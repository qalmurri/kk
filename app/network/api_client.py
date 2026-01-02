import requests
from core.session import Session

class ApiClient:
    TIMEOUT = 10

    @classmethod
    def build_base_url(cls):
        return f"http://{Session.server_ip}"

    @classmethod
    def headers(cls):
        headers = {
            "Content-Type": "application/json"
        }
        if Session.token:
            headers["Authorization"] = f"Bearer {Session.token}"
        return headers

    @classmethod
    def post(cls, endpoint: str, json: dict):
        url = cls.build_base_url() + endpoint
        response = requests.post(
            url,
            json=json,
            headers=cls.headers(),
            timeout=cls.TIMEOUT
        )
        response.raise_for_status()
        return response.json()

    @classmethod
    def get(cls, endpoint: str):
        url = cls.build_base_url() + endpoint
        response = requests.get(
            url,
            headers=cls.headers(),
            timeout=cls.TIMEOUT
        )
        response.raise_for_status()
        return response.json()
