from PySide6.QtCore import QObject, Signal, Slot
from core.api_client import ApiClient
from core.session import Session

class LogoutWorker(QObject):
    success = Signal()
    error = Signal(str)
    finished = Signal()

    @Slot()
    def run(self):
        try:
            refresh = Session.get_refresh_token()

            ApiClient.request(
                "POST",
                "/logout/",
                json={"refresh": refresh},
                retry=False
            )

            self.success.emit()

        except Exception as e:
            self.error.emit(str(e))

        finally:
            self.finished.emit()