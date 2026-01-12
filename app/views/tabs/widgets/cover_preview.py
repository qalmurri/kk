from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene
from views.tabs.widgets.graphics_view import InteractiveGraphicsView
from PySide6.QtGui import QPixmap, QBrush, QColor, QPen
from PySide6.QtCore import Qt, QRectF
import requests
import os

class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        self.view = InteractiveGraphicsView()
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        
        # Opsional: Beri background gelap pada view agar canvas putih terlihat kontras
        self.view.setStyleSheet("background-color: #2b2b2b;")
        layout.addWidget(self.view)

    def update_preview(self, cover: dict):
        self.scene.clear()

        # 1. AMBIL DATA
        thickness = max(cover.get("length", 10), 1)
        height = max(cover.get("height", 250), 50)
        width = max(cover.get("width", 160), 50)
        thumbnail_url = cover.get("thumbnail")

        # 2. LOGIKA POSISI (Flat Spread)
        # Urutan standar percetakan: [Back Cover] [Spine] [Front Cover]
        back_x = 0
        spine_x = width
        front_x = width + thickness

        # Pen untuk garis bantu lipatan (dotted line)
        fold_pen = QPen(QColor("#808080"))
        fold_pen.setStyle(Qt.DashLine)
        fold_pen.setWidth(1)

        # 3. RENDER COMPONENTS
        
        # --- BACK COVER ---
        self.scene.addRect(
            QRectF(back_x, 0, width, height),
            pen=fold_pen,
            brush=QBrush(QColor("#fcfcfc"))
        )

        # --- SPINE (Punggung) ---
        self.scene.addRect(
            QRectF(spine_x, 0, thickness, height),
            pen=fold_pen,
            brush=QBrush(QColor("#f0f0f0"))
        )

        # --- FRONT COVER ---
        pixmap = self._safe_load_pixmap(thumbnail_url, width, height)
        if pixmap:
            # Gunakan Pixmap jika ada gambar
            front = self.scene.addPixmap(pixmap)
            front.setOffset(front_x, 0)
        else:
            # Placeholder jika gambar kosong
            self.scene.addRect(
                QRectF(front_x, 0, width, height),
                pen=fold_pen,
                brush=QBrush(QColor("#ffffff"))
            )

        # 4. SET BOUNDING AREA
        # Pastikan scene hanya sebesar total (width*2 + thickness) x height
        total_width = (width * 2) + thickness
        self.scene.setSceneRect(0, 0, total_width, height)
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def _safe_load_pixmap(self, path, w, h):
            if not path:
                return None

            pix = QPixmap()
        
        # LOGIKA 1: Jika ini URL Internet
            if path.startswith(("http://", "https://")):
                try:
                    resp = requests.get(path, timeout=3)
                    if pix.loadFromData(resp.content):
                        return pix.scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                except Exception as e:
                    print(f"Error loading URL: {e}")
                    return None
        
        # LOGIKA 2: Jika ini File Lokal
            else:
                if os.path.exists(path):
                    if pix.load(path): # QPixmap bisa langsung load file path
                        return pix.scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                else:
                    print(f"File tidak ditemukan: {path}")
        
            return None
