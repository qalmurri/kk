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
        self.setWindowTitle("Enterprise App PySide6")
        self.setCentralWidget(self.main_controller.view) 
        self.load_settings()

    def load_settings(self):
        """Memuat ukuran dan posisi jendela terakhir."""
        width = self.settings.value("main/window_width", 850, type=int) 
        height = self.settings.value("main/window_height", 650, type=int)
        self.resize(width, height)

    def closeEvent(self, event):
        """Dipanggil saat jendela ditutup. Simpan preferensi dan token."""
        self.settings.setValue("main/window_width", self.width())
        self.settings.setValue("main/window_height", self.height())

        api_client = self.main_controller.auth_manager.get_api_client()
        refresh_token = api_client.get_refresh_token()

        if refresh_token:
            self.settings.setValue("auth/refresh_token", refresh_token) 
        else:
            self.settings.remove("auth/refresh_token")

        self.main_controller.save_column_widths()
        self.settings.sync()
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    QApplication.setOrganizationName("PROJECT_2025_KK") 
    QApplication.setApplicationName("EnterpriseApp")
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
        print("Token ditemukan. Mencoba Auto-Login...")
        new_access_token = api_client.refresh_access_token(saved_refresh_token)

        if new_access_token:
            # Jika refresh berhasil, gunakan token lama dan baru untuk otentikasi manager
            # Catatan: Kita memanggil authenticate_user dengan dua token di sini.
            auth_manager.authenticate_user(
                access_token=new_access_token,
                refresh_token=saved_refresh_token
            )
            print("Auto-Login berhasil menggunakan Refresh Token.")
            # Lanjutkan menampilkan Main Window
            main_window = AppMainWindow(settings, main_controller)
            main_window.show()
            main_controller.fetch_data()
            auth_manager.logged_out.connect(main_window.close)
            sys.exit(app.exec())
        else:
            print("Auto-Login gagal (Refresh Token expired atau invalid). Memerlukan login manual.")
            settings.remove("auth/refresh_token") # Hapus token yang rusak
    elif saved_refresh_token and not api_client.get_base_url():
        print("Gagal Auto-Login: Refresh Token ditemukan, tetapi BASE URL belum pernah disimpan.")

    # --- PERBAIKAN 5: Logic Login Manual (Jika Auto-Login Gagal/Tidak Ada Token) ---
    if not main_window:
        login_dialog = LoginDialog(login_controller.view)
        auth_manager.logged_in.connect(login_dialog.accept) 
        result = login_dialog.exec()
        
        if result == QDialog.Accepted:
            main_window = AppMainWindow(settings, main_controller)
            main_window.show()
            main_controller.fetch_data()
            auth_manager.logged_out.connect(main_window.close)
            sys.exit(app.exec())
        else:
            sys.exit(0)

if __name__ == "__main__":
    main()