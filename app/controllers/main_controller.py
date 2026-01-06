from PySide6.QtCore import QThread
from core.session import AppSession
from app.workers.login_worker import LogoutWorker

class MainController:
    def __init__(self, view):
        self.view = view
        self.view.logout_btn.clicked.connect(self.logout)

    def logout(self):
        self.view.set_loading(True)

        self.thread = QThread()
        self.worker = LogoutWorker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_success)
        self.worker.error.connect(self.on_error)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def on_success(self):
        AppSession.clear_auth()
        self.view.set_loading(False)
        self.view.on_logout_success()

    def on_error(self, message: str):
        AppSession.clear_auth()
        self.view.set_loading(False)
        self.view.on_logout_success()
