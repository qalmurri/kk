from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene
from views.tabs.widgets.graphics_view import InteractiveGraphicsView
from PySide6.QtGui import QPixmap, QBrush, QColor, QTransform
from PySide6.QtCore import Qt, QRectF
import requests

class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        # Setup View & Scene
        self.view = InteractiveGraphicsView()
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        layout.addWidget(self.view)

    def update_preview(self, cover: dict):
        self.scene.clear()

        # 1. DATA
        thickness = max(cover.get("length", 10), 1)
        height = max(cover.get("height", 250), 50)
        width = max(cover.get("width", 160), 50)
        thumbnail_url = cover.get("thumbnail")

        # 2. COORDINATES (2D Spread Layout)
        # Susunan: [BACK] [SPINE] [FRONT]
        back_x = 0
        spine_x = width
        front_x = width + thickness

        transform = QTransform()
        transform.shear(-0.2, 0)
        transform.rotate(-5)

        # 3. RENDER COMPONENTS
        # Back
        back = self.scene.addRect(QRectF(back_x, 0, width, height), brush=QBrush(QColor("#dcdcdc")))
        back.setTransform(transform)
        
        # Spine
        spine = self.scene.addRect(QRectF(spine_x, 0, thickness, height), brush=QBrush(QColor("#a8a8a8")))
        spine.setTransform(transform)
        
        # Front
        pixmap = self._safe_load_pixmap(thumbnail_url, width, height)
        if pixmap:
            front = self.scene.addPixmap(pixmap)
            front.setOffset(front_x, 0)
        else:
            front = self.scene.addRect(QRectF(front_x, 0, width, height), brush=QBrush(QColor("#f0f0f0")))
        front.setTransform(transform)
        front.setZValue(2)

        self.scene.setSceneRect(self.scene.itemsBoundingRect())

    def _safe_load_pixmap(self, url, w, h):
        if not url or not url.startswith("http"): return None
        try:
            resp = requests.get(url, timeout=3)
            pix = QPixmap()
            if pix.loadFromData(resp.content):
                return pix.scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        except: return None
        return None
