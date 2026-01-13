from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene
<<<<<<< HEAD
from PySide6.QtGui import QPixmap, QBrush, QColor, QTransform
=======
from views.tabs.widgets.graphics_view import InteractiveGraphicsView
<<<<<<< HEAD
from PySide6.QtGui import (
    QPixmap, QBrush, QColor, QTransform
)
>>>>>>> 8dd6eeec919d09620d51292c12b30ea6954b996f
=======
from PySide6.QtGui import QPixmap, QBrush, QColor, QPen
>>>>>>> 47cf6c39715e954809c925e366bd156519e0eea0
from PySide6.QtCore import Qt, QRectF
import requests
import os

class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
<<<<<<< HEAD

<<<<<<< HEAD
=======
=======
        
>>>>>>> 47cf6c39715e954809c925e366bd156519e0eea0
        self.view = InteractiveGraphicsView()
>>>>>>> 8dd6eeec919d09620d51292c12b30ea6954b996f
        self.scene = QGraphicsScene(self)
<<<<<<< HEAD
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

=======
        self.view.setScene(self.scene)
        
        # Opsional: Beri background gelap pada view agar canvas putih terlihat kontras
        self.view.setStyleSheet("background-color: #2b2b2b;")
>>>>>>> 47cf6c39715e954809c925e366bd156519e0eea0
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

<<<<<<< HEAD
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
=======
    def _safe_load_pixmap(self, path, w, h):
            if not path:
>>>>>>> 47cf6c39715e954809c925e366bd156519e0eea0
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
>>>>>>> 8dd6eeec919d09620d51292c12b30ea6954b996f
