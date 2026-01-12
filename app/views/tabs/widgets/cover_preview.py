from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene
from PySide6.QtGui import QPixmap, QBrush, QColor, QTransform
from PySide6.QtCore import Qt, QRectF
import requests


class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.scene = QGraphicsScene(self)
        from views.tabs.widgets.graphics_view import InteractiveGraphicsView
        self.view = InteractiveGraphicsView()
        self.view.setScene(self.scene)

        layout.addWidget(self.view)

    # =========================================
    def update_preview(self, cover: dict):
        self.scene.clear()

        h = cover.get("height", 25)
        w = cover.get("width", 16)
        t = cover.get("length", 2)

        thumbnail = self._load_thumbnail(cover.get("thumbnail"), w*2 + t, h)

        if thumbnail:
            back, spine, front = self._slice(thumbnail, w, h, t)
        else:
            back = spine = front = None

        # ================= TRANSFORM =================
        iso = QTransform()
        iso.shear(-0.4, 0)
        iso.rotate(-12)

        x0, y0 = 0, 0

        # ================= BACK =================
        back_item = self.scene.addPixmap(
            back if back else self._solid_pixmap(w, h, "#b0b0b0")
        )
        back_item.setTransform(iso)
        back_item.setOffset(x0, y0)
        back_item.setZValue(0)

        # ================= SPINE =================
        spine_item = self.scene.addPixmap(
            spine if spine else self._solid_pixmap(t, h, "#909090")
        )
        spine_item.setTransform(iso)
        spine_item.setOffset(x0 + w, y0)
        spine_item.setZValue(1)

        # ================= FRONT =================
        front_item = self.scene.addPixmap(
            front if front else self._solid_pixmap(w, h, "#e0e0e0")
        )
        front_item.setTransform(iso)
        front_item.setOffset(x0 + w + t, y0)
        front_item.setZValue(2)

        self.scene.setSceneRect(self.scene.itemsBoundingRect())

    # =========================================
    def _slice(self, pixmap, w, h, t):
        back = pixmap.copy(0, 0, w, h)
        spine = pixmap.copy(w, 0, t, h)
        front = pixmap.copy(w + t, 0, w, h)
        return back, spine, front

    # =========================================
    def _solid_pixmap(self, w, h, color):
        pix = QPixmap(w, h)
        pix.fill(QColor(color))
        return pix

    # =========================================
    def _load_thumbnail(self, url, w, h):
        if not url:
            return None
        try:
            r = requests.get(url, timeout=3)
            pix = QPixmap()
            if pix.loadFromData(r.content):
                return pix.scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        except Exception:
            pass
        return None
