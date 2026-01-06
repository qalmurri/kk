from PySide6.QtCore import QObject, Signal, Slot
from core.api_client import ApiClient

class ProfileWorker(QObject):
    success = Signal(dict)
    error = Signal(str)
    finished = Signal()

    @Slot()
    def run(self):
        try:
            resp = ApiClient.request("GET", "/profile/")

            if resp.status_code != 200:
                raise Exception("Unauthorized")
            
            self.success.emit(resp.json())

        except Exception as e:
            self.error.emit(str(e))

        finally:
            self.finished.emit()