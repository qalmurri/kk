import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QSettings, Qt # <-- Tambahkan QDialog
# Import kelas-kelas Anda
from core.api_client import APIClient
from core.auth_manager import AuthManager
from controllers.main_controller import MainController
from controllers.login_controller import LoginController # Asumsi Anda memiliki LoginController

# Import UI yang baru
from views.login_dialog import LoginDialog # <-- Jendela Login Mandiri

class AppMainWindow(QMainWindow): # Ubah nama kelas utama menjadi AppMainWindow
    """Jendela Utama Aplikasi (Hanya Main Dashboard)."""
    def __init__(self, settings: QSettings, main_controller: MainController):
        super().__init__()
        self.settings = settings
        self.main_controller = main_controller
        self.setWindowTitle("Enterprise App PySide6")
        
        # Atur Central Widget ke View dari Main Controller
        self.setCentralWidget(self.main_controller.view) 
        
        # Muat ukuran jendela dari QSettings (default besar)
        self.load_settings()

    def load_settings(self):
        """Memuat ukuran dan posisi jendela terakhir."""
        width = self.settings.value("main/window_width", 850, type=int) 
        height = self.settings.value("main/window_height", 650, type=int)
        self.resize(width, height)
        
    def closeEvent(self, event):
        """Dipanggil saat jendela ditutup. Simpan preferensi."""
        self.settings.setValue("main/window_width", self.width())
        self.settings.setValue("main/window_height", self.height())
        self.main_controller.save_column_widths() 
        super().closeEvent(event)

# main.py (Di dalam class AppMainWindow)

    def closeEvent(self, event):
        """Dipanggil saat jendela ditutup. Simpan preferensi dan token."""
        # ... (Simpan ukuran jendela dan kolom) ...
        
        # --- SIMPAN TOKEN AKTIF ---
        token = self.main_controller.auth_manager.get_token() # <-- Kita perlu metode ini
        self.settings.setValue("auth/token", token)
        
        # --------------------------
        
        self.main_controller.save_column_widths() 
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    
    # --- SETUP CONFIG & KLIEN ---
    QApplication.setOrganizationName("PROJECT_2025_KK") 
    QApplication.setApplicationName("EnterpriseApp")
    settings = QSettings() 
    
    api_client = APIClient()
    auth_manager = AuthManager(api_client)

    # --- SETUP CONTROLLERS ---
    # LoginController: Mengelola logika UI LoginWidget
    login_controller = LoginController(api_client, auth_manager) 
    # MainController: Mengelola logika Main Dashboard
    main_controller = MainController(api_client, auth_manager) 
    
    # ----------------------------------------------------
    # 1. TAMPILKAN JENDELA LOGIN MODAL (KECIL)
    # ----------------------------------------------------
    


# main.py (di dalam fungsi main())


    # ... (setup app, settings, api_client, auth_manager) ...
    
    # --- PROSES AUTO-LOGIN (BARU) ---
    saved_token = settings.value("auth/token", None)
    
    if saved_token:
        print("Token ditemukan. Mencoba Auto-Login...")
        # Lakukan validasi token di APIClient (opsional, untuk memastikan token valid)
        # Untuk kasus sederhana, kita anggap token yang disimpan valid.
        auth_manager.authenticate_user(saved_token) # Gunakan token yang disimpan
        
        # 2. TAMPILKAN MAIN WINDOW (BESAR)
        main_window = AppMainWindow(settings, main_controller)
        main_window.show()
        main_controller.fetch_data()

        auth_manager.logged_out.connect(main_window.close)
        
        sys.exit(app.exec()) # Keluar dari fungsi main dan jalankan loop aplikasi
        
    login_dialog = LoginDialog(login_controller.view)
    
    # Sinyal harus dihubungkan agar dialog tahu kapan harus ditutup
    auth_manager.logged_in.connect(login_dialog.accept) 
    
    # Tampilkan dialog dan tunggu
    result = login_dialog.exec()
    
    if result == QDialog.Accepted:
        def handle_logout():
            main_window.close() # Tutup Main Window
        # Login berhasil, auth_manager sudah memiliki token.
        
        # 2. TAMPILKAN MAIN WINDOW (BESAR)
        main_window = AppMainWindow(settings, main_controller)
        main_window.show()
        
        # Muat data segera setelah Main Window muncul
        main_controller.fetch_data()

        auth_manager.logged_out.connect(main_window.close)
        
        sys.exit(app.exec())
    else:
        # Login dibatalkan atau dialog ditutup tanpa login
        sys.exit(0)

if __name__ == "__main__":
    main()