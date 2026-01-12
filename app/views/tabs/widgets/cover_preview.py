from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene
<<<<<<< HEAD
from PySide6.QtGui import QPixmap, QBrush, QColor, QTransform
=======
from views.tabs.widgets.graphics_view import InteractiveGraphicsView
from PySide6.QtGui import (
    QPixmap, QBrush, QColor, QTransform
)
>>>>>>> 8dd6eeec919d09620d51292c12b30ea6954b996f
from PySide6.QtCore import Qt, QRectF
import requests


class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

<<<<<<< HEAD
=======
        self.view = InteractiveGraphicsView()
>>>>>>> 8dd6eeec919d09620d51292c12b30ea6954b996f
        self.scene = QGraphicsScene(self)
        from views.tabs.widgets.graphics_view import InteractiveGraphicsView
        self.view = InteractiveGraphicsView()
        self.view.setScene(self.scene)
<<<<<<< HEAD

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
=======
        self.view.setRenderHint(self.view.renderHints())
        self.view.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.view)

    # =====================================================
    def update_preview(self, cover: dict):
        self.scene.clear()

        # ========= RAW DATA =========
        thickness = max(cover.get("length", 5), 1)
        height = max(cover.get("height", 200), 50)
        width = max(cover.get("width", 120), 50)

        thumbnail = cover.get("thumbnail")

        # ========= SCALE (UI FRIENDLY) =========
        SCALE = 1
        thickness *= SCALE
        height *= SCALE
        width *= SCALE

        # ========= BASE POS =========
        origin_x = 0
        origin_y = 0

        # ========= LOAD THUMBNAIL =========
        front_pixmap = self._safe_load_pixmap(thumbnail, width, height)

        # ========= TRANSFORM (FAKE 3D) =========
        transform = QTransform()
        transform.shear(-0.3, 0)   # perspective
        transform.rotate(-8)

        # ========= BACK COVER =========
        back = self.scene.addRect(
            QRectF(origin_x, origin_y, width, height),
            brush=QBrush(QColor("#c8c8c8"))
        )
        back.setTransform(transform)
        back.setZValue(0)

        # ========= SPINE =========
        spine = self.scene.addRect(
            QRectF(origin_x - thickness, origin_y, thickness, height),
            brush=QBrush(QColor("#a8a8a8"))
        )
        spine.setTransform(transform)
        spine.setZValue(1)

        # ========= FRONT COVER =========
        if front_pixmap:
            front = self.scene.addPixmap(front_pixmap)
            front.setOffset(origin_x + thickness, origin_y)
        else:
            front = self.scene.addRect(
                QRectF(origin_x + thickness, origin_y, width, height),
                brush=QBrush(QColor("#e0e0e0"))
            )

        front.setTransform(transform)
        front.setZValue(2)

        # ========= SHADOW =========
        shadow = self.scene.addRect(
            QRectF(origin_x + thickness + 12, origin_y + 10, width, height),
            brush=QBrush(QColor(0, 0, 0, 35))
>>>>>>> 8dd6eeec919d09620d51292c12b30ea6954b996f
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

<<<<<<< HEAD
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
=======
    # =====================================================
    def _safe_load_pixmap(self, url, w, h):
        """Return QPixmap or None (never crash)."""
        if not url:
            return None

        try:
            resp = requests.get(url, timeout=3)
            resp.raise_for_status()

            pixmap = QPixmap()
            if not pixmap.loadFromData(resp.content):
                return None

            return pixmap.scaled(
                w, h,
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )

        except Exception:
            return None
>>>>>>> 8dd6eeec919d09620d51292c12b30ea6954b996f
