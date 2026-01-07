import requests
from core.session import Session

class ApiClient:
    @classmethod
    def request(cls, method, endpoint, *, json=None, retry=True):
        url = f"http://{Session.get_backend_ip()}{endpoint}"

        headers = {}
        access = Session.get_access_token()

        if access:
            headers["Authorization"] = f"Bearer {access}"

        response = requests.request(
            method,
            url,
            json=json,
            headers=headers,
            timeout=5
        )

        if response.status_code == 401 and retry:
            if cls._refresh_token():
                return cls.request(method, endpoint, json=json, retry=False)
            
        return response
    
    @classmethod
    def _refresh_token(cls):
        refresh = Session.get_refresh_token()
        if not refresh:
            return False
        
        response = requests.post(
            f"http://{Session.get_backend_ip()}/token/refresh/",
            json={"refresh": refresh},
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            Session.set_tokens(
                access=data["access"],
                refresh=refresh
            )
            return True
        
        return False

    @classmethod
    def ensure_valid_access_token(cls) -> bool:
        access = Session.get_access_token()
        if not access:
            return False
        
        # Optional: decode exp JWT (kalau mau advance)
        # untuk sekarang: refresh selalu kalau mau WS
        return cls._refresh_token()