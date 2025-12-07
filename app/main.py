import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from core.api_client import APIClient
from core.auth_manager import AuthManager 
from controllers.login_controller import LoginController
from controllers.main_controller import MainController 

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enterprise App PySide6")
        
        self.api_client = APIClient()
        self.auth_manager = AuthManager(self.api_client) 
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        # --- Inisialisasi Controller ---
        # Pastikan MainController sudah menerima 3 argumen (self, api, auth)
        self.login_controller = LoginController(self.api_client, self.auth_manager)
        self.main_controller = MainController(self.api_client, self.auth_manager)    

        # --- Tambahkan View ke Stack ---
        self.stack.addWidget(self.login_controller.view) # Index 0: Login
        self.stack.addWidget(self.main_controller.view)  # Index 1: Main App
        
        # --- Menghubungkan Sinyal ---
        self.auth_manager.logged_in.connect(self.show_main_window)
        self.auth_manager.logged_out.connect(self.show_login_window) # <--- Sinyal yang menyebabkan error
        
        self.show()

    def show_main_window(self):
        """Dipanggil setelah login berhasil."""
        print("Login berhasil! Menampilkan Main Window dan memuat data.")
        self.stack.setCurrentIndex(1) 
        self.main_controller.fetch_data()

    # METHOD INI YANG HILANG DAN PERLU DITAMBAHKAN:
    def show_login_window(self):
        """Dipanggil setelah logout atau kegagalan otentikasi."""
        print("Beralih ke jendela Login.")
        self.stack.setCurrentIndex(0) 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec())