from PySide6.QtCore import QObject, Signal
from core.api_client import APIClient
from core.auth_manager import AuthManager # <--- BARU
from views.ui_login import LoginWidget

class LoginController(QObject):
    """Menangani logika proses login."""
    login_successful = Signal()
    login_failed = Signal(str)

    def __init__(self, api_client: APIClient, auth_manager: AuthManager):
        super().__init__()
        self.api_client = api_client
        self.auth_manager = auth_manager # <--- BARU
        self.view = LoginWidget()
        
        # Menghubungkan tombol UI ke metode kontrol
        self.view.button_login.clicked.connect(self.handle_login)
        
    def handle_login(self):
        username = self.view.input_username.text()
        password = self.view.input_password.text()
        
        self.view.label_status.setText("Sedang mencoba login...")
        
        token = self.api_client.login(username, password)
        
        if token:
            # Panggil AuthManager untuk menyelesaikan proses otentikasi
            self.auth_manager.authenticate_user(token) 
            # AuthManager akan memancarkan sinyal logged_in yang ditangkap oleh main.py
        else:
            self.view.label_status.setText("Login Gagal. Cek kredensial (user/pass).")