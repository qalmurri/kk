from PySide6.QtCore import QObject, QThread, Slot
from workers.login_worker import LoginWorker
from core.session import Session

class LoginController(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.thread = None
        self.worker = None

        self.view.login_btn.clicked.connect(self.login)

    @Slot()
    def login(self):
        self.view.set_loading(True)

        self.thread = QThread(self)
        self.worker = LoginWorker(
            self.view.username_input.text(),
            self.view.password_input.text()
        )

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.success.connect(self._success)
        self.worker.error.connect(self._error)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    @Slot(dict)
    def _success(self, data: dict):
        Session.set_tokens(data["access"], data["refresh"])
        self.view.set_loading(False)
        self.view.on_login_success()

    @Slot(str)
    def _error(self, msg: str):
        self.view.set_loading(False)
        self.view.show_error(msg)
