from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import Qt, Signal


class InteractiveGraphicsView(QGraphicsView):
    # Sinyal untuk memberitahu Previewer bahwa rotasi berubah
    rotationChanged = Signal(float, float) 

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self._last_pos = None
        
        # Simpan rotasi dalam derajat
        self.rot_x = -15.0 # Sedikit menunduk
        self.rot_y = -25.0 # Sedikit menyamping
        self._scale = 1.0

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._last_pos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._last_pos and event.buttons() & Qt.LeftButton:
            dx = event.pos().x() - self._last_pos.x()
            dy = event.pos().y() - self._last_pos.y()

            # Gerakan X mouse merotasi sumbu Y buku
            # Gerakan Y mouse merotasi sumbu X buku
            self.rot_y += dx * 0.5
            self.rot_x -= dy * 0.5 

            self.rotationChanged.emit(self.rot_x, self.rot_y)
            self._last_pos = event.pos()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self._last_pos = None
        super().mouseReleaseEvent(event)

    def wheelEvent(self, event):
        factor = 1.15 if event.angleDelta().y() > 0 else 0.85
        self.scale(factor, factor)