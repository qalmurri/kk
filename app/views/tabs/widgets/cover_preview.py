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
            # 1. AMBIL DATA DASAR
            thickness = max(cover.get("length", 10), 1)
            height = max(cover.get("height", 250), 50)
            width = max(cover.get("width", 160), 50)
            thumbnail_url = cover.get("thumbnail")

            # 2. HITUNG TOTAL LEBAR (Full Spread)
            # Total = Lebar Belakang + Lebar Punggung + Lebar Depan
            total_width = (width * 2) + thickness
            back_x = 0
            spine_x = width
            front_x = width + thickness

            # 3. LOAD GAMBAR UNTUK SELURUH AREA
            # Sekarang kita kirim total_width ke fungsi loader
            full_pixmap = self._safe_load_pixmap(thumbnail_url, total_width, height)
            if full_pixmap:
                # Masukkan satu gambar besar mulai dari titik 0 (paling kiri/Back Cover)
                full_cover = self.scene.addPixmap(full_pixmap)
                full_cover.setOffset(0, 0)
                full_cover.setZValue(0)
            else:
                # Jika gambar tidak ada, buat kotak placeholder abu-abu
                self.scene.addRect(QRectF(0, 0, total_width, height), brush=QBrush(QColor("#f0f0f0")))

            # 4. TAMBAHKAN GARIS BANTU (GUIDES)
            # Agar user tahu di mana letak lipatan Spine, kita gambar garis di atas gambar
            guide_pen = QPen(QColor(255, 255, 255, 150)) # Putih transparan
            guide_pen.setStyle(Qt.DashLine)
            
            # Garis Lipatan 1 (Antara Back dan Spine)
            self.scene.addLine(spine_x, 0, spine_x, height, guide_pen)
            # Garis Lipatan 2 (Antara Spine dan Front)
            self.scene.addLine(front_x, 0, front_x, height, guide_pen)

            # 5. SET BOUNDING AREA
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