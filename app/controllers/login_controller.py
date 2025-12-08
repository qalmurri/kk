from PySide6.QtCore import QObject, Signal, QSettings
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
        base_url = self.view.input_url.text()
        username = self.view.input_username.text()
        password = self.view.input_password.text()

        if not base_url or not username or not password:
            self.view.label_status.setText("URL, Username, dan Password wajib diisi.")
            return
        
        self.view.label_status.setText("Sedang mencoba login...")

        self.api_client.set_base_url(base_url)
        
        access_token = self.api_client.login(username, password)
        if access_token:
            settings = QSettings()
            settings.setValue("app/base_url", base_url)
            settings.sync()

            refresh_token = self.api_client.get_refresh_token()
            if refresh_token:
                self.auth_manager.authenticate_user(
                    access_token=access_token, 
                    refresh_token=refresh_token
                )
                self.view.input_username.clear()
                self.view.input_password.clear()
                self.login_successful.emit() # Sinyal login sukses
            else:
                 # Ini seharusnya tidak terjadi jika login API berhasil
                self.view.label_status.setText("Login Gagal. Server tidak mengirim Refresh Token.")
        else:
            self.view.label_status.setText("Login Gagal. Cek kredensial (user/pass) atau koneksi server.")