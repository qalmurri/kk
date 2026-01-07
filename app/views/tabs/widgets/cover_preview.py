from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene
from views.tabs.widgets.graphics_view import InteractiveGraphicsView
from PySide6.QtGui import (
    QPixmap, QBrush, QColor, QTransform
)
from PySide6.QtCore import Qt, QRectF
import requests


class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.view = InteractiveGraphicsView()
        self.scene = QGraphicsScene(self)

        self.view.setScene(self.scene)
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
        )
        shadow.setZValue(-1)

        self.scene.setSceneRect(self.scene.itemsBoundingRect())

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
