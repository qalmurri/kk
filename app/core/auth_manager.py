from PySide6.QtCore import QObject, Signal, QSettings

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

# core/auth_manager.py (Modifikasi logout_user)

    def logout_user(self):
        """
        Melakukan logout (memanggil API logout Django) dan membersihkan status.
        """
        # 1. Panggil Endpoint Server (opsional)
        self._api_client.logout() 
        
        # 2. Bersihkan status lokal
        self._api_client.set_token(None)
        self._is_authenticated = False
        self._current_user_data = {}
        
        # 3. Hapus token dari QSettings (Penting untuk mencegah auto-login)
        settings = QSettings()
        settings.remove("auth/token") # Hapus token yang tersimpan
        
        self.logged_out.emit()
        
    def is_authenticated(self):
        """Memeriksa apakah user saat ini sudah login."""
        return self._is_authenticated

    def get_user_data(self):
        """Mendapatkan data user yang sedang login."""
        return self._current_user_data
    
# core/auth_manager.py (Tambahkan metode ini)

    def get_token(self):
        """Mendapatkan token aktif."""
        # Mengasumsikan token disimpan di self._api_client._token atau sejenisnya
        # Jika Anda tidak menyimpan token di AuthManager, ambil dari APIClient
        return self._api_client.get_token() # <-- Asumsikan APIClient memiliki get_token()