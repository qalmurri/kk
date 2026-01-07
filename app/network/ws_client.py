from PySide6.QtWebSockets import QWebSocket
from PySide6.QtNetwork import QAbstractSocket
from PySide6.QtCore import QObject, QUrl, Signal
from core.session import Session
from core.api_client import ApiClient

class WebSocketClient(QObject):
    connected = Signal()
    disconnected = Signal()
    message_received = Signal(dict)
    error = Signal(str)

    def __init__(self):
        super().__init__()
        self.socket = QWebSocket()

        self.socket.connected.connect(self.connected.emit)
        self.socket.disconnected.connect(self.disconnected.emit)
        self.socket.textMessageReceived.connect(self._on_message)
        self.socket.errorOccurred.connect(
            lambda e: self.error.emit(str(e))
        )

    def connect(self):
        if not ApiClient.ensure_valid_access_token():
            self.error.emit("Unable to refresh access token")
            return

        token = Session.get_access_token()
        if not token:
            self.error.emit("No access token")
            return

        url = QUrl(
            f"ws://{Session.get_backend_ip()}/ws/presence/?token={token}"
        )
        self.socket.open(url)

    def disconnect(self):
        if self.socket.state() == QAbstractSocket.ConnectedState:
            self.socket.close()

    def _on_message(self, message: str):
        try:
            import json
            self.message_received.emit(json.loads(message))
        except Exception:
            self.error.emit("Invalid WS message")