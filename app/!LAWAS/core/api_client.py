import requests
import re

class APIClient:
    """Klien HTTP yang menangani komunikasi API dan otentikasi."""
    def __init__(self):
        self._access_token = None
        self._refresh_token = None
        self._base_url = "http://127.0.0.1:8000/"
        self.session = requests.Session()
        print("APIClient: Klien HTTP diinisialisasi.")

    def set_base_url(self, base_url: str):
        """Menyetel BASE URL dan memastikan diakhiri dengan slash (/)."""
        if not base_url.endswith('/'):
            base_url += '/'
        self._base_url = base_url
        print(f"APIClient: BASE URL diatur ke: {self._base_url}")
        
    def get_base_url(self):
        """Mengambil BASE URL yang sedang aktif."""
        return self._base_url

    def _get_url(self, endpoint: str):
        """Helper untuk membuat URL lengkap dari BASE_URL."""
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
        print(f"APIClient: Mencoba login pengguna '{username}' ke: {url}")
        
        try:
            response = self.session.post(url, json=payload, timeout=10)
            print(f"APIClient: Respon Login diterima, Status: {response.status_code}")
            response.raise_for_status()
            
            response_data = response.json()
            access_token = response_data.get('access')
            refresh_token = response_data.get('refresh')

            if access_token and refresh_token:
                print(f"APIClient: Login sukses. Token Access di terima: {access_token[:10]}...")
                print(f"APIClient: Token Refresh di terima: {refresh_token[:10]}...")

                return (access_token, refresh_token)
            else:
                print("APIClient: Login berhasil (Status 200/201), tetapi access/refresh token tidak ditemukan dalam respons JSON.")
                return None
            
        except requests.exceptions.HTTPError as e:
            print(f"APIClient ERROR: Login gagal (HTTP Error): {e.response.status_code}. Cek kredensial.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"APIClient CRITICAL ERROR: Login gagal (Koneksi/Lainnya). Pastikan server berjalan di {self._base_url}. Detail: {e}")
            return None

    def set_access_token(self, access_token: str = None):
        """Menyetel access token dan mengupdate header session."""
        self._access_token = access_token
        
        if access_token:
            print("APIClient: Header 'Authorization' disetel dengan Access Token baru.")
            self.session.headers.update({
                'Authorization': f'Bearer {access_token}'
            })
        else:
            if 'Authorization' in self.session.headers:
                del self.session.headers['Authorization']
                print("APIClient: Header 'Authorization' dihapus (Token dibersihkan).")

    def set_refresh_token(self, refresh_token: str = None):
        """Menyetel refresh token."""
        self._refresh_token = refresh_token
        if refresh_token:
            print("APIClient: Refresh Token disimpan di memori.")
        else:
            print("APIClient: Refresh Token dibersihkan dari memori.")

    def set_token(self, access_token: str = None, refresh_token: str = None):
        """Menyetel access dan refresh token, serta mengupdate header session."""
        print(f"APIClient: set_token dipanggil. Distribusi Access Token...")
        self.set_access_token(access_token)
        self.set_refresh_token(refresh_token)
        
    def get_items(self):
        """Mengambil data skrip (item) dari server API."""
        if self.get_token() is None: 
            print("APIClient WARNING: Kegagalan GET items: Access Token belum disetel. Melewatkan permintaan.")
            return []
            
        url = self.ITEMS_URL
        print(f"APIClient: Mengambil data items dari: {url}")
        
        try:
            response = self.session.get(url, timeout=10) 
            print(f"APIClient: Respon GET items diterima, Status: {response.status_code}")
            response.raise_for_status()
            
            data = response.json()
            print(f"APIClient: Data berhasil diambil dari API. Jumlah item: {len(data) if isinstance(data, list) else 'tidak diketahui'}.")
            return data
                
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response.status_code == 401:
                print("APIClient ERROR: Kegagalan GET items: Unauthorized (Token mungkin tidak valid/kedaluwarsa).")
            else:
                print(f"APIClient ERROR: Kegagalan GET items (Koneksi/Lainnya). Detail: {e}")
            
            return []

    def create_item(self, data):
        pass

    def logout(self):
        url = self.LOGOUT_URL
        refresh_token = self.get_refresh_token() 
        
        if not refresh_token:
            print("APIClient WARNING: Logout gagal: Refresh token tidak ditemukan secara lokal. Melanjutkan logout lokal.")
            return True 
        
        payload = {"refresh": refresh_token}

        print(f"APIClient: Mencoba logout server dengan menghapus Refresh Token ke: {url}")
        
        try:
            response = self.session.post(url, json=payload, timeout=5) 
            print(f"APIClient: Server response for logout: {response.status_code}")
            
            if response.status_code in [200, 204]:
                print("APIClient: Logout berhasil di server (Refresh Token di-blacklist).")
                return True
            elif response.status_code == 400:
                print("APIClient: Logout gagal di server (Token Invalid/Expired), tetapi kita anggap sukses untuk logout lokal.")
                return True
            else:
                print(f"APIClient: Logout gagal di server, status: {response.status_code}. Melanjutkan logout lokal.")
                return True 
                
        except requests.exceptions.RequestException as e:
            print(f"APIClient ERROR: Error koneksi saat logout: {e}. Melanjutkan logout lokal.")
            return True
        
    def get_token(self):
        return self._access_token
    
    def get_refresh_token(self):
        return self._refresh_token
    
    def refresh_access_token(self, refresh_token):
        """Menggunakan refresh token untuk mendapatkan access token baru."""
        url = self.REFRESH_URL
        payload = {"refresh": refresh_token}
        
        print(f"APIClient: Mencoba refresh Access Token ke: {url}")
        
        try:
            response = self.session.post(url, json=payload, timeout=10)
            print(f"APIClient: Respon Refresh diterima, Status: {response.status_code}")
            response.raise_for_status()
            
            response_data = response.json()
            new_access_token = response_data.get('access')
            
            if new_access_token:
                print("APIClient: Token Access baru berhasil diambil.")
                return new_access_token
            
            print("APIClient: Refresh sukses (Status 200), tetapi Access Token baru tidak ditemukan.")
            return None

        except requests.exceptions.RequestException as e:
            print(f"APIClient ERROR: Gagal refresh token. Token mungkin invalid, expired, atau koneksi terputus. Detail: {e}")
            return None