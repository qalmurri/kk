from PySide6.QtCore import QObject, Signal, QSettings

class AuthManager(QObject):
    """
    Mengelola status otentikasi user (token) dan data user.
    Ini adalah Single Source of Truth (SSOT) untuk status login.
    """
    logged_in = Signal()
    logged_out = Signal()

    def __init__(self, api_client):
        super().__init__()
        self._api_client = api_client
        self._is_authenticated = False
        self._current_user_data = {}
        print("AuthManager: Instance diinisialisasi.")

    def authenticate_user(self, access_token: str, refresh_token: str, user_data: dict = None):
        """
        Dipanggil setelah login berhasil atau auto-login sukses. Mengatur token dan status.
        """
        print("AuthManager: Mengatur token dan status autentikasi.")
        self._api_client.set_token(access_token, refresh_token)

        settings = QSettings()
        settings.setValue("auth/refresh_token", refresh_token)
        settings.sync()

        self._is_authenticated = True
        self._current_user_data = user_data if user_data else {}
        self.logged_in.emit()
        print("AuthManager: Sinyal logged_in dikirim.")

    def logout_user(self):
        """
        Melakukan logout (memanggil API logout Django) dan membersihkan status.
        """
        print("AuthManager: Memulai proses logout...")
        self._api_client.logout() 

        self._api_client.set_token(None, None)

        self._is_authenticated = False
        self._current_user_data = {}

        settings = QSettings()
        settings.remove("auth/refresh_token")
        print("AuthManager: Token dihapus dari QSettings.")
        self.logged_out.emit()
        print("AuthManager: Sinyal logged_out dikirim.")
        
    def is_authenticated(self):
        """Memeriksa apakah user saat ini sudah login."""
        return self._is_authenticated

    def get_user_data(self):
        """Mendapatkan data user yang sedang login."""
        return self._current_user_data

    def get_token(self):
        """Mendapatkan token aktif."""
        return self._api_client.get_token()
    
    def get_api_client(self):
        """Mengembalikan instance APIClient."""
        return self._api_client