from core.session import Session
from utils.workers import LoginWorker

class AuthController:
    def __init__(self, view):
        self.view = view
        self.view.login_btn.clicked.connect(self.login)
        self.worker = None

    def login(self):
        ip = self.view.ip_input.text().strip()
        username = self.view.username_input.text().strip()
        password = self.view.password_input.text().strip()

        if not ip or not username or not password:
            self.view.show_error("Semua field wajib diisi")
            return

        self.view.set_loading(True)

        self.worker = LoginWorker(ip, username, password)
        self.worker.success.connect(self.on_success)
        self.worker.error.connect(self.on_error)
        self.worker.start()

    def on_success(self, data: dict):
        Session.token = data.get("token")
        Session.user = data.get("user")

        self.view.set_loading(False)
        self.view.on_login_success()

    def on_error(self, message: str):
        self.view.set_loading(False)
        self.view.show_error(message)
