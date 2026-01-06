import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QSettings
from core.api_client import APIClient
from core.auth_manager import AuthManager
from controllers.main_controller import MainController
from controllers.login_controller import LoginController
from views.login_dialog import LoginDialog

class AppMainWindow(QMainWindow):
    """Jendela Utama Aplikasi (Hanya Main Dashboard)."""
    def __init__(self, settings: QSettings, main_controller: MainController):
        super().__init__()
        self.settings = settings
        self.main_controller = main_controller
        self.setWindowTitle("KK")
        self.setCentralWidget(self.main_controller.view) 
        self.load_settings()
        print("AppMainWindow: Jendela Utama diinisialisasi dan ditampilkan.")

    def load_settings(self):
        """Memuat ukuran, posisi, dan status jendela (normal/maximized) terakhir."""
        
        # --- LOGIKA LAMA (Hanya resize) ---
        # width = self.settings.value("main/window_width", 850, type=int) 
        # height = self.settings.value("main/window_height", 650, type=int)
        # self.resize(width, height)
        
        # --- LOGIKA BARU (Menggunakan Geometry dan Status Maximize) ---
        geometry = self.settings.value("main/geometry", None)
        is_maximized = self.settings.value("main/is_maximized", False, type=bool)
        
        if geometry:
            self.restoreGeometry(geometry)
            print("AppMainWindow: Memuat posisi dan ukuran jendela dari QSettings.")
        else:
             self.resize(850, 650) # Ukuran default jika tidak ada settings

        if is_maximized:
            self.showMaximized()
            print("AppMainWindow: Memuat status jendela: Maximized.")
        else:
            # Jika tidak maximized, pastikan ia show normal, karena showMaximized() telah dipanggil
            # Catatan: Kita memanggil .show() di main() nanti, jadi ini aman.
            pass

    def closeEvent(self, event):
        """Dipanggil saat jendela ditutup. Simpan preferensi dan token."""
        print("AppMainWindow: Jendela ditutup. Menyimpan pengaturan...")
        self.settings.setValue("main/geometry", self.saveGeometry())
        self.settings.setValue("main/is_maximized", self.isMaximized())

        api_client = self.main_controller.auth_manager.get_api_client()
        refresh_token = api_client.get_refresh_token()

        if refresh_token:
            self.settings.setValue("auth/refresh_token", refresh_token) 
            print("AppMainWindow: Refresh Token disimpan ke QSettings.")
        else:
            self.settings.remove("auth/refresh_token")
            print("AppMainWindow: Refresh Token dihapus dari QSettings.")

        self.main_controller.save_column_widths()
        self.settings.sync()
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    QApplication.setOrganizationName("PROJECT_2025_KK") 
    QApplication.setApplicationName("EnterpriseApp")
    print("Main: Aplikasi dimulai.")
    
    settings = QSettings() 
    api_client = APIClient()

    saved_base_url = settings.value("app/base_url", None)
    if saved_base_url:
        api_client.set_base_url(saved_base_url)

    auth_manager = AuthManager(api_client)
    login_controller = LoginController(api_client, auth_manager) 

    if saved_base_url:
        login_controller.view.input_url.setText(saved_base_url)
        
    main_controller = MainController(api_client, auth_manager) 

    saved_refresh_token = settings.value("auth/refresh_token", None)
    main_window = None

    if saved_refresh_token and api_client.get_base_url():
        print("Main: Token ditemukan. Mencoba Auto-Login...")
        new_access_token = api_client.refresh_access_token(saved_refresh_token)

        if new_access_token:
            print("Main: Token Access Baru diterima dari Refresh API.")
            auth_manager.authenticate_user(
                access_token=new_access_token,
                refresh_token=saved_refresh_token
            )
            print("Main: Auto-Login berhasil menggunakan Refresh Token.")
            
            main_window = AppMainWindow(settings, main_controller)
            main_window.show()
            main_controller.fetch_data()
            auth_manager.logged_out.connect(main_window.close)
            sys.exit(app.exec())
        else:
            print("Main: Auto-Login gagal (Refresh Token expired atau invalid). Memerlukan login manual.")
            settings.remove("auth/refresh_token")
            print("Main: Token Refresh yang rusak dihapus dari QSettings.")
    elif saved_refresh_token and not api_client.get_base_url():
        print("Main WARNING: Gagal Auto-Login: Refresh Token ditemukan, tetapi BASE URL belum pernah disimpan. Memerlukan login manual.")

    if not main_window:
        print("Main: Memulai proses Login Manual...")
        login_dialog = LoginDialog(login_controller.view)
        auth_manager.logged_in.connect(login_dialog.accept) 
        result = login_dialog.exec()
        
        if result == QDialog.Accepted:
            print("Main: Login Manual Sukses. Menampilkan Main Window.")
            main_window = AppMainWindow(settings, main_controller)
            main_window.show()
            main_controller.fetch_data()
            auth_manager.logged_out.connect(main_window.close)
            sys.exit(app.exec())
        else:
            print("Main: Login dibatalkan oleh user.")
            sys.exit(0)

if __name__ == "__main__":
    main()