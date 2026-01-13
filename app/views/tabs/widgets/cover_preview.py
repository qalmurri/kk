from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene, QGraphicsItem
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
        self.view.setStyleSheet("background-color: #2b2b2b;")
        layout.addWidget(self.view)

        # State untuk transformasi
        self.x_offset = 0
        self.y_offset = 0
        self.zoom_level = 1.0
        
        self.last_cover_data = None
        self.base_pixmap = None 

    def update_preview(self, cover: dict = None, x=None, y=None, zoom=None):
        # 1. Update state dan proteksi nilai 0 dari model
        if cover and cover != self.last_cover_data:
            self.last_cover_data = cover
            # Ambil nilai awal dari model
            self.x_offset = cover.get("x_axis", 0)
            self.y_offset = cover.get("y_axis", 0)
            
            # Proteksi jika zoom di model adalah 0, ubah ke 1.0
            z_val = cover.get("zoom", 0)
            self.zoom_level = z_val if z_val > 0 else 1.0
            
            thumbnail_url = cover.get("thumbnail")
            self.base_pixmap = self._load_raw_pixmap(thumbnail_url)
            
            # Reset view fit jika ganti buku
            if hasattr(self, '_initial_fit'):
                delattr(self, '_initial_fit')

        if x is not None: self.x_offset = x
        if y is not None: self.y_offset = y
        if zoom is not None: self.zoom_level = zoom

        self.render_scene()

    def render_scene(self):
        self.scene.clear()
        if not self.last_cover_data:
            return

        thickness = max(self.last_cover_data.get("length", 10), 1)
        height = max(self.last_cover_data.get("height", 250), 50)
        width = max(self.last_cover_data.get("width", 160), 50)
        total_width = (width * 2) + thickness

        # --- LOGIKA CLIPPING ---
        
        # 2. Buat "Canvas" (Rect Putih) sebagai PARENT
        # Kita simpan ke variabel canvas agar bisa menampung child
        canvas = self.scene.addRect(
            QRectF(0, 0, total_width, height), 
            brush=QBrush(QColor("#ffffff")), 
            pen=QPen(Qt.NoPen)
        )
        
        # AKTIFKAN CLIPPING: Anak-anak dari canvas ini tidak akan terlihat jika keluar batas
        canvas.setFlag(QGraphicsItem.ItemClipsChildrenToShape)

        # 3. Tambahkan Gambar sebagai CHILD dari canvas
        if self.base_pixmap:
            scaled_base = self.base_pixmap.scaledToHeight(height, Qt.SmoothTransformation)
            
            # Masukkan pixmap ke dalam scene, tapi set canvas sebagai parent
            pixmap_item = self.scene.addPixmap(scaled_base)
            pixmap_item.setParentItem(canvas) # <--- KUNCI UTAMA
            
            pixmap_item.setScale(self.zoom_level)
            
            center_x = scaled_base.width() / 2
            center_y = scaled_base.height() / 2
            pixmap_item.setTransformOriginPoint(center_x, center_y)

            # Posisi sekarang relatif terhadap canvas (0,0 adalah pojok kiri atas canvas)
            default_x = (total_width - scaled_base.width()) / 2
            default_y = (height - scaled_base.height()) / 2
            
            pixmap_item.setPos(default_x + self.x_offset, default_y + self.y_offset)

        # 4. Tambahkan Garis Bantu (Guides) 
        # Tetap jadikan child dari canvas agar ikut terpotong jika diperlukan, 
        # tapi letakkan di atas gambar (Z-Value)
        guide_pen = QPen(QColor(100, 100, 100, 200))
        guide_pen.setStyle(Qt.DashLine)
        
        spine_x = width
        front_x = width + thickness
        
        l1 = self.scene.addLine(spine_x, 0, spine_x, height, guide_pen)
        l2 = self.scene.addLine(front_x, 0, front_x, height, guide_pen)
        l1.setParentItem(canvas)
        l2.setParentItem(canvas)
        l1.setZValue(2)
        l2.setZValue(2)

        # 5. Finalisasi View
        self.scene.setSceneRect(0, 0, total_width, height)
        if not hasattr(self, '_initial_fit'):
            self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
            self._initial_fit = True

    def _load_raw_pixmap(self, path):
        if not path or path == "https://": return None
        pix = QPixmap()
        try:
            if path.startswith(("http://", "https://")):
                resp = requests.get(path, timeout=5)
                pix.loadFromData(resp.content)
            elif os.path.exists(path):
                pix.load(path)
            return pix if not pix.isNull() else None
        except:
            return None