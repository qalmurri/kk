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
        token = self.main_controller.auth_manager.get_token()
        self.settings.setValue("auth/token", token)
        self.settings.setValue("main/window_width", self.width())
        self.settings.setValue("main/window_height", self.height())
        api_client = self.main_controller.auth_manager.get_api_client()
        refresh_token = api_client.get_refresh_token()
        self.settings.setValue("auth/token", refresh_token) # Menggunakan kunci lama
        self.main_controller.save_column_widths()
        self.settings.sync()
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    QApplication.setOrganizationName("PROJECT_2025_KK") 
    QApplication.setApplicationName("EnterpriseApp")
    settings = QSettings() 
    api_client = APIClient()
    auth_manager = AuthManager(api_client)
    login_controller = LoginController(api_client, auth_manager) 
    main_controller = MainController(api_client, auth_manager) 
    saved_token = settings.value("auth/token", None)
    if saved_token:
        print("Token ditemukan. Mencoba Auto-Login...")
        auth_manager.authenticate_user(saved_token)
        main_window = AppMainWindow(settings, main_controller)
        main_window.show()
        main_controller.fetch_data()
        auth_manager.logged_out.connect(main_window.close)
        sys.exit(app.exec())
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