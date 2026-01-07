from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import Qt


class InteractiveGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

        self._last_pos = None
        self._rotation = 0.0
        self._scale = 1.0

    # =============================
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._last_pos = event.pos()
        super().mousePressEvent(event)

    # =============================
    def mouseMoveEvent(self, event):
        if self._last_pos:
            dx = event.pos().x() - self._last_pos.x()

            # UPDATE ROTATION
            self._rotation += dx * 0.3

            # APPLY TRANSFORM
            self._apply_transform()

            self._last_pos = event.pos()

        super().mouseMoveEvent(event)

    # =============================
    def mouseReleaseEvent(self, event):
        self._last_pos = None
        super().mouseReleaseEvent(event)

    # =============================
    def wheelEvent(self, event):
        zoom_factor = 1.15

        if event.angleDelta().y() > 0:
            self._scale *= zoom_factor
        else:
            self._scale /= zoom_factor

        self._apply_transform()

    # =============================
    def _apply_transform(self):
        self.resetTransform()
        self.scale(self._scale, self._scale)
        self.rotate(self._rotation)
