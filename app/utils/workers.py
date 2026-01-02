from PySide6.QtCore import QThread, Signal

class LoginWorker(QThread):
    success = Signal(dict)
    error = Signal(str)

    def __init__(self, ip, username, password):
        super().__init__()
        self.ip = ip
        self.username = username
        self.password = password

    def run(self):
        from network.auth_service import AuthService

        ok, result = AuthService.login(
            self.ip,
            self.username,
            self.password
        )

        if ok:
            self.success.emit(result)
        else:
            self.error.emit(result)

class LoadScriptsWorker(QThread):
    success = Signal(list)
    error = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        from network.data_service import DataService

        try:
            response = DataService.fetch_scripts()
            data = response.get("data", [])
            self.success.emit(data)
        except Exception as e:
            self.error.emit(str(e))
