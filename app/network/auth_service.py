from network.api_client import ApiClient
from core.session import Session

class AuthService:

    @staticmethod
    def login(ip: str, username: str, password: str):
        Session.server_ip = ip

        try:
            response = ApiClient.post(
                "/login/",
                json={
                    "username": username,
                    "password": password
                }
            )
            return True, response

        except Exception as e:
            return False, str(e)
