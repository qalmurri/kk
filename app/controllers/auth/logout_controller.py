from PySide6.QtCore import QObject, QThread, Slot
from workers.logout_worker import LogoutWorker
from core.session import Session

class LogoutController(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.thread = None
        self.worker = None

    @Slot()
    def logout(self):
        self.thread = QThread(self)
        self.worker = LogoutWorker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self._cleanup)

        self.thread.start()

    @Slot()
    def _cleanup(self):
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()
            
        self.worker.deleteLater()
        self.thread.deleteLater()

        Session.clear_tokens()

        from views.auth.login_window import LoginWindow
        login = LoginWindow()
        login.show()



        self.view.close()


