import requests

class APIClient:
    """Klien HTTP yang menangani komunikasi API dan otentikasi."""
    BASE_URL = "http://127.0.0.1:8000/" 
    LOGIN_URL = BASE_URL + "login/"
    LOGOUT_URL = BASE_URL + "logout/"
    ITEMS_URL = BASE_URL + "scripts/"

    def __init__(self):
        self._access_token = None     # Access token (untuk header 'Bearer')
        self._refresh_token = None    # Refresh token (untuk logout dan refresh)
        self.session = requests.Session()
        
    def set_token(self, access_token: str = None, refresh_token: str = None):
        """Menyetel access dan refresh token, serta mengupdate header session."""
        self._access_token = access_token
        self._refresh_token = refresh_token
        if access_token:
            self.session.headers.update({
                'Authorization': f'Bearer {access_token}'
            })
        else:
            if 'Authorization' in self.session.headers:
                del self.session.headers['Authorization']

    def login(self, username, password):
        """Melakukan permintaan POST untuk mendapatkan token login dari server backend."""
        url = self.LOGIN_URL
        payload = {'username': username, 'password': password}
        print(f"Mencoba login ke: {url}")
        
        try:
            response = self.session.post(url, json=payload, timeout=10)
            response.raise_for_status()
            
            response_data = response.json()
            print(f"Server Login Success Response Data: {response_data}")

            access_token = response_data.get('access')
            refresh_token = response_data.get('refresh') # <-- BARU: Ambil refresh token

            if access_token and refresh_token:
                print("Login berhasil via API.")
                # self.set_token harus disesuaikan jika menyimpan refresh token
                # Saat ini, mari kita asumsikan Anda menyimpan KEDUA token:
                self.set_token(access_token, refresh_token) # <--- Perlu modifikasi set_token
                print(f"DEBUG: Access Token tersimpan: {self._access_token[:10]}...")
                print(f"DEBUG: Refresh Token tersimpan: {self._refresh_token[:10]}...")
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
        
    def get_items(self):
            """
            Mengambil data skrip (item) dari server API yang sesungguhnya.
            Permintaan ini menggunakan Token otentikasi yang telah disetel.
            """
            url = self.ITEMS_URL
            print(f"Mengambil data dari: {url}")
            
            try:
                response = self.session.get(url, timeout=10) 
                response.raise_for_status()
                
                data = response.json()
                print("Data berhasil diambil dari API.")
                return data
                
            except requests.exceptions.RequestException as e:
                if self.get_token is None:
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