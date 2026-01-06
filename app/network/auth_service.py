# network/auth_service.py
from network.api_client import ApiClient

class AuthService:
    @staticmethod
    def login(username: str, password: str) -> dict:
        return ApiClient.post(
            "login/",
            {
                "username": username,
                "password": password
            }
        )
