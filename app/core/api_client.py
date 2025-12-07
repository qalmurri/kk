import requests

class APIClient:
    """Klien HTTP yang menangani komunikasi API dan otentikasi."""
    # Ganti BASE_URL menjadi endpoint root API Anda jika berbeda,
    # tetapi untuk login kita akan menggunakan URL lengkap.
    BASE_URL = "http://127.0.0.1:8000/" 
    LOGIN_URL = BASE_URL + "login/" # Endpoint login
    ITEMS_URL = BASE_URL + "scripts/" # Asumsi endpoint data
    
    # ----------------------------------------------------------------

    def __init__(self):
        self._token = None 
        self.session = requests.Session()
        
    def set_token(self, token: str):
        """Menyimpan dan mengatur header otorisasi (Token Auth DRF)."""
        self._token = token
        # Pastikan server DRF Anda menggunakan TokenAuthentication
        self.session.headers.update({
            'Authorization': f'Token {self._token}' 
        })

    def login(self, username, password):
        """Melakukan permintaan POST untuk mendapatkan token login dari server backend."""
        url = self.LOGIN_URL
        payload = {'username': username, 'password': password}
        print(f"Mencoba login ke: {url}") # Tambahkan log untuk debugging
        
        try:
            # Kirim permintaan POST ke server Django
            response = self.session.post(url, json=payload, timeout=10)
            response.raise_for_status() # Akan memicu exception jika status code 4xx atau 5xx
            
            # Asumsi DRF mengembalikan {'token': 'string_token'}
            token = response.json().get('token')
            if token:
                print("Login berhasil via API.")
                return token
            else:
                print("Login berhasil, tetapi token tidak ditemukan dalam respons.")
                return None
            
        except requests.exceptions.HTTPError as e:
            # Menangani error seperti 401 Unauthorized (kredensial salah)
            print(f"Login gagal (HTTP Error): {e.response.status_code}")
            return None
        except requests.exceptions.RequestException as e:
            # Menangani error koneksi (server tidak jalan)
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
                # Menggunakan self.session yang sudah memiliki header 'Authorization: Token xxx'
                response = self.session.get(url, timeout=10) 
                response.raise_for_status() # Cek status code
                
                # Asumsi DRF mengembalikan list of dicts
                data = response.json()
                print("Data berhasil diambil dari API.")
                return data
                
            except requests.exceptions.RequestException as e:
                # Ini akan menangkap kegagalan koneksi atau HTTPError (misalnya 401 Unauthorized)
                if self._token is None:
                    print("Kegagalan GET items: Token belum disetel. Pastikan Anda sudah login.")
                elif hasattr(e, 'response') and e.response.status_code == 401:
                    print("Kegagalan GET items: Unauthorized (Token mungkin tidak valid/kedaluwarsa).")
                else:
                    print(f"Kegagalan GET items (Koneksi/Lainnya): {e}")
                
                # Jika gagal, kita mengembalikan list kosong, bukan Mock Data lagi
                return []

    # Implementasi CRUD lainnya tetap sama...
    def create_item(self, data):
        pass
    # ...
# core/api_client.py (Tambahkan endpoint ini)

    def logout(self):
        """Panggil endpoint logout di server Django."""
        url = f"{self.BASE_URL}/logout/"
        
        try:
            # Gunakan header yang sudah disetel oleh set_token
            response = self.session.post(url, timeout=5)
            
            if response.status_code in [200, 204]:
                print("Logout berhasil di server.")
                return True
            else:
                print(f"Logout gagal di server, status: {response.status_code}")
                # Tetap anggap logout lokal berhasil meskipun server gagal
                return True 
                
        except requests.exceptions.RequestException as e:
            print(f"Error koneksi saat logout: {e}")
            return True # Tetap logout lokal agar user bisa mencoba lagi

# Tambahkan get_token di APIClient
    def get_token(self):
        return self._token