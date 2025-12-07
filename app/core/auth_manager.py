from PySide6.QtCore import QObject, Signal

class AuthManager(QObject):
    """
    Mengelola status otentikasi user (token) dan data user.
    Ini adalah Single Source of Truth (SSOT) untuk status login.
    """
    # Signal yang dipancarkan ketika status otentikasi berubah
    logged_in = Signal()
    logged_out = Signal()

    def __init__(self, api_client):
        super().__init__()
        self._api_client = api_client
        self._is_authenticated = False
        self._current_user_data = {} # Bisa menyimpan username, email, dll.

    def authenticate_user(self, token: str, user_data: dict = None):
        """
        Dipanggil setelah login berhasil. Mengatur token dan status.
        """
        self._api_client.set_token(token) # Memberikan token ke API client
        self._is_authenticated = True
        self._current_user_data = user_data if user_data else {}
        self.logged_in.emit()

    def logout_user(self):
        """
        Melakukan logout (bisa memanggil API logout Django jika ada)
        dan membersihkan status.
        """
        self._api_client.set_token(None)
        self._is_authenticated = False
        self._current_user_data = {}
        # TODO: Di sini Anda bisa memanggil api_client.logout() jika ada endpoint logout.
        self._api_client.MOCK_TOKEN = None # Untuk pengujian mock
        self.logged_out.emit()
        
    def is_authenticated(self):
        """Memeriksa apakah user saat ini sudah login."""
        return self._is_authenticated

    def get_user_data(self):
        """Mendapatkan data user yang sedang login."""
        return self._current_user_data