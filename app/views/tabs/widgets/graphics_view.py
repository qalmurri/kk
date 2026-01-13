from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPainter

class InteractiveGraphicsView(QGraphicsView):
    rotationChanged = Signal(float, float) 

    def __init__(self, parent=None):
        super().__init__(parent)

        # --- TAMBAHKAN RENDER HINTS UNTUK KUALITAS ---
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setRenderHint(QPainter.TextAntialiasing)
        # --------------------------------------------
# --- TAMBAHKAN BARIS INI UNTUK MENGHILANGKAN BAYANGAN ---
        # Memaksa view membersihkan seluruh area setiap frame
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        # -------------------------------------------------------
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self._last_pos = None
        
        # Rotasi default
        self.rot_x = -20.0 
        self.rot_y = -30.0 
        self._scale = 1.0

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._last_pos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._last_pos and event.buttons() & Qt.LeftButton:
            dx = event.pos().x() - self._last_pos.x()
            dy = event.pos().y() - self._last_pos.y()

            self.rot_y -= dx * 0.5 
            self.rot_x += dy * 0.5 
            self.rotationChanged.emit(self.rot_x, self.rot_y)
            self._last_pos = event.pos()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self._last_pos = None
        super().mouseReleaseEvent(event)

    def wheelEvent(self, event):
        # Zoom view (opsional, jika ingin zoom kamera)
        factor = 1.15 if event.angleDelta().y() > 0 else 0.85
        self.scale(factor, factor)