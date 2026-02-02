import requests
from core.config import DEFAULT_BACKEND_IP
from core.session import Session

class APIClient:
    def get(self, endpoint, params=None):
        url = f"http://{DEFAULT_BACKEND_IP}{endpoint}"
        response = Session.get(url, params=params)
        response.raise_for_status()
        return response.json()

api_client=APIClient()
