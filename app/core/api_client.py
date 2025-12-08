import requests
import re

class APIClient:
    """Klien HTTP yang menangani komunikasi API dan otentikasi."""
    def __init__(self):
        self._access_token = None     # Access token (untuk header 'Bearer')
        self._refresh_token = None    # Refresh token (untuk logout dan refresh)
        self._base_url = "http://127.0.0.1:8000/" # Nilai default awal
        self.session = requests.Session()

    def set_base_url(self, base_url: str):
        """Menyetel BASE URL dan memastikan diakhiri dengan slash (/)."""
        if not base_url.endswith('/'):
            base_url += '/'
        self._base_url = base_url
        print(f"BASE URL diatur ke: {self._base_url}")
        
    def get_base_url(self):
        """Mengambil BASE URL yang sedang aktif."""
        return self._base_url

    def _get_url(self, endpoint: str):
        """Helper untuk membuat URL lengkap dari BASE_URL."""
        # Membersihkan endpoint dari leading slash jika ada
        endpoint = re.sub(r'^/', '', endpoint) 
        return f"{self._base_url}{endpoint}"

    @property
    def LOGIN_URL(self):
        return self._get_url("login/")
    
    @property
    def LOGOUT_URL(self):
        return self._get_url("logout/")

    @property
    def ITEMS_URL(self):
        return self._get_url("scripts/")

    @property
    def REFRESH_URL(self):
        return self._get_url("token/refresh/")

    def login(self, username, password):
        """Melakukan permintaan POST untuk mendapatkan token login dari server backend."""
        url = self.LOGIN_URL
        payload = {'username': username, 'password': password}
        print(f"Mencoba login ke: {url}")
        
        try:
            response = self.session.post(url, json=payload, timeout=10)
            response.raise_for_status()
            
            response_data = response.json()
            access_token = response_data.get('access')
            refresh_token = response_data.get('refresh')

            if access_token and refresh_token:
                print(f"access token di terima: {access_token[:10]}...")
                print(f"refresh token di terima: {refresh_token[:10]}...")
                self.set_access_token(access_token)
                self.set_refresh_token(refresh_token)

                return access_token # Kembalikan access token untuk otentikasi
            else:
                # Ini terjadi jika respons 200 OK tetapi token tidak ada
                print("Login berhasil, tetapi access/refresh token tidak ditemukan dalam respons.")
                return None
            
        except requests.exceptions.HTTPError as e:
            print(f"Login gagal (HTTP Error): {e.response.status_code}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Login gagal (Koneksi/Lainnya): Pastikan server Django berjalan di {self.BASE_URL}. Error: {e}")
            return None

    def set_access_token(self, access_token: str = None):
        """Menyetel access token dan mengupdate header session."""
        self._access_token = access_token
        
        if access_token:
            # Hanya set header saat access token ada
            self.session.headers.update({
                'Authorization': f'Bearer {access_token}'
            })
        else:
            # Membersihkan header saat access token dihapus (misalnya, saat logout)
            if 'Authorization' in self.session.headers:
                del self.session.headers['Authorization']

    def set_refresh_token(self, refresh_token: str = None):
        """Menyetel refresh token (tidak mempengaruhi header session)."""
        self._refresh_token = refresh_token

    def set_token(self, access_token: str = None, refresh_token: str = None):
        """Menyetel access dan refresh token, serta mengupdate header session."""
        print(f"set_token: distribusi access token: {access_token}...")
        print(f"set_token: distribusi refresh token: {refresh_token}...")
        self.set_access_token(access_token)
        self.set_refresh_token(refresh_token)
        
    def get_items(self):
            """
            Mengambil data skrip (item) dari server API yang sesungguhnya.
            Permintaan ini menggunakan Token otentikasi yang telah disetel.
            """
            if self.get_token() is None: 
                print("Kegagalan GET items: Token belum disetel. Pastikan Anda sudah login.")
                return []
            
            url = self.ITEMS_URL
            print(f"Mengambil data dari: {url}")
            
            try:
                response = self.session.get(url, timeout=10) 
                response.raise_for_status()
                
                data = response.json()
                print("Data berhasil diambil dari API.")
                return data
                
            except requests.exceptions.RequestException as e:
                if self.get_token() is None:
                    print("Kegagalan GET items: Token belum disetel. Pastikan Anda sudah login.")
                elif hasattr(e, 'response') and e.response.status_code == 401:
                    print("Kegagalan GET items: Unauthorized (Token mungkin tidak valid/kedaluwarsa).")
                else:
                    print(f"Kegagalan GET items (Koneksi/Lainnya): {e}")
                
                return []

    def create_item(self, data):
        pass

    def logout(self):
        url = self.LOGOUT_URL
        refresh_token = self.get_refresh_token() # Ambil refresh token yang tersimpan
        
        if not refresh_token:
            print("Logout gagal: Refresh token tidak ditemukan secara lokal.")
            return True # Tetap logout lokal
        
        payload = {"refresh": refresh_token} # <-- Kirim sebagai payload

        try:
            # Kirim POST dengan payload
            response = self.session.post(url, json=payload, timeout=5) 
            print(f"Server response for logout: {response.status_code}")
            
            if response.status_code in [200, 204]:
                print("Logout berhasil di server (token di-blacklist).")
                return True
            elif response.status_code == 400:
                print("Logout gagal di server (Token Invalid/Expired).")
                return True # Asumsikan logout lokal tetap harus terjadi
            else:
                print(f"Logout gagal di server, status: {response.status_code}")
                return True 
                
        except requests.exceptions.RequestException as e:
            print(f"Error koneksi saat logout: {e}")
            return True
        
    def get_token(self):
        return self._access_token
    
    def get_refresh_token(self):
        return self._refresh_token
    
    def refresh_access_token(self, refresh_token):
        """Menggunakan refresh token untuk mendapatkan access token baru."""
        url = self.REFRESH_URL
        payload = {"refresh": refresh_token}
        
        try:
            response = self.session.post(url, json=payload, timeout=10)
            response.raise_for_status()
            
            response_data = response.json()
            new_access_token = response_data.get('access')
            
            if new_access_token:
                # Hanya set access token baru. Refresh token lama dipertahankan.
                self.set_access_token(new_access_token)
                print("Token Access berhasil diperbarui.")
                return new_access_token
            return None

        except requests.exceptions.RequestException as e:
            print(f"Gagal refresh token. Token lama mungkin invalid atau expired. Error: {e}")
            return None