from PySide6.QtCore import QObject, Signal, Slot
from core.api_client import ApiClient

class LoginWorker(QObject):
    success = Signal(dict)
    error = Signal(str)
    finished = Signal() 

    def __init__(self, username: str, password: str):
        super().__init__()
        self.username = username
        self.password = password

    @Slot()
    def run(self):
        try:
            resp = ApiClient.request(
                "POST",
                "/login/",
                json={
                    "username": self.username,
                    "password": self.password
                }
            )

            if resp.status_code != 200:
                raise Exception("Login gagal")

            self.success.emit(resp.json())

        except Exception as e:
            self.error.emit(str(e))

        finally:
            self.finished.emit()