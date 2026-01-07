from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
)
from PySide6.QtGui import QPixmap, QBrush, QColor
from PySide6.QtCore import Qt, QRectF

class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.view = QGraphicsView()
        self.scene = QGraphicsScene(self)

        self.view.setScene(self.scene)
        self.view.setRenderHint(self.view.renderHints())

        layout.addWidget(self.view)

    def update_preview(self, cover: dict):
        self.scene.clear()

        # === DATA ===
        length = cover.get("length", 1) * 60
        height = cover.get("height", 1) * 80
        width = cover.get("width", 1) * 20

        x_axis = cover.get("x_axis", 0)
        y_axis = cover.get("y_axis", 0)
        thumbnail = cover.get("thumbnail")

        # === FRONT COVER ===
        front_rect = QRectF(0, 0, length, height)

        if thumbnail:
            pixmap = QPixmap()  
            pixmap.loadFromData(self._load_image(thumbnail))
            pixmap = pixmap.scaled(
                length, height,
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            front = self.scene.addPixmap(pixmap)
            front.setOffset(x_axis, y_axis)
        else:
            front = self.scene.addRect(
                front_rect,
                brush=QBrush(QColor("#d0d0d0"))
            )

        # === SPINE (WIDTH) ===
        spine = self.scene.addRect(
            QRectF(-width, 0, width, height),
            brush=QBrush(QColor("#b0b0b0"))
        )

        # === SIMPLE DEPTH SHADOW ===
        shadow = self.scene.addRect(
            QRectF(5, 5, length, height),
            brush=QBrush(QColor(0, 0, 0, 40))
        )
        shadow.setZValue(-1)

        self.scene.setSceneRect(self.scene.itemsBoundingRect())

    def _load_image(self, url: str) -> bytes:
        # SEMENTARA dummy, nanti bisa ganti cache downloader
        import requests
        return requests.get(url).content
