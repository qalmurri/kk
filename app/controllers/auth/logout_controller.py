from PySide6.QtCore import QObject, QThread, Slot
from workers.logout_worker import LogoutWorker
from core.session import Session

class LogoutController(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.thread = None
        self.worker = None

        self.view.logout_btn.clicked.connect(self.logout)

    @Slot()
    def logout(self):
        self.thread = QThread(self)
        self.worker = LogoutWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.success.connect(self._done)
        self.worker.error.connect(self._done)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    @Slot()
    def _done(self):
        Session.clear_tokens()

        from views.auth.login_window import LoginWindow
        login = LoginWindow()
        login.show()

        self.view.close()
