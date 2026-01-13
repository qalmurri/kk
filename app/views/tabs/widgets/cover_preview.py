from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene, QGraphicsPolygonItem
from views.tabs.widgets.graphics_view import InteractiveGraphicsView
from PySide6.QtGui import QPixmap, QBrush, QColor, QPen, QTransform, QPolygonF
from PySide6.QtCore import Qt, QPointF, QRectF
import requests
import math, requests, os

class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.view = InteractiveGraphicsView()
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.view.setStyleSheet("background-color: #1e1e1e;")
        layout.addWidget(self.view)

        self.view.rotationChanged.connect(self.update_rotation)
        self.rot_x = -15.0
        self.rot_y = -25.0
        self.last_cover_data = None
        self.base_pixmap = None

    def update_rotation(self, rx, ry):
        self.rot_x, self.rot_y = rx, ry
        self.render_scene()

    def update_preview(self, cover: dict = None, x=None, y=None, zoom=None):
        if cover:
            self.last_cover_data = cover
            self.base_pixmap = self._load_raw_pixmap(cover.get("thumbnail"))
        self.render_scene()

    def project(self, x, y, z):
        rad_x = math.radians(self.rot_x)
        rad_y = math.radians(self.rot_y)
        # Rotasi Y
        nx = x * math.cos(rad_y) + z * math.sin(rad_y)
        nz = -x * math.sin(rad_y) + z * math.cos(rad_y)
        # Rotasi X
        ny = y * math.cos(rad_x) - nz * math.sin(rad_x)
        final_z = y * math.sin(rad_x) + nz * math.cos(rad_x)
        factor = 800 / (800 + final_z)
        return QPointF(nx * factor, ny * factor), final_z

    def render_scene(self):
        self.scene.clear()
        if not self.last_cover_data: return

        w = self.last_cover_data.get("width", 160)
        h = self.last_cover_data.get("height", 250)
        t = self.last_cover_data.get("length", 20)
        cx, cy, cz = w/2, h/2, t/2

        # DEFINISI TITIK SUDUT (Vertices) - Membentuk Box Solid
        # Sisi Depan (Front) - Z = -cz
        f_v = [(0-cx, 0-cy, 0-cz), (w-cx, 0-cy, 0-cz), (w-cx, h-cy, 0-cz), (0-cx, h-cy, 0-cz)]
        # Sisi Belakang (Back) - Z = cz
        b_v = [(w-cx, 0-cy, t-cz), (0-cx, 0-cy, t-cz), (0-cx, h-cy, t-cz), (w-cx, h-cy, t-cz)]
        # Sisi Punggung (Spine) - X = -cx
        s_v = [(0-cx, 0-cy, t-cz), (0-cx, 0-cy, 0-cz), (0-cx, h-cy, 0-cz), (0-cx, h-cy, t-cz)]
        # Sisi Kertas (Side/Pages) - X = w-cx
        p_v = [(w-cx, 0-cy, 0-cz), (w-cx, 0-cy, t-cz), (w-cx, h-cy, t-cz), (w-cx, h-cy, 0-cz)]
        # Sisi Atas (Top)
        t_v = [(0-cx, 0-cy, t-cz), (w-cx, 0-cy, t-cz), (w-cx, 0-cy, 0-cz), (0-cx, 0-cy, 0-cz)]

        # List semua face untuk di-sort berdasarkan kedalaman (Z-depth)
        faces = [
            (f_v, QColor("#ffffff"), "front"),
            (b_v, QColor("#ffffff"), "back"),
            (s_v, QColor("#eeeeee"), "spine"),
            (p_v, QColor("#f0f0f0"), "pages"),
            (t_v, QColor("#ffffff"), "top")
        ]

        # Z-Sorting: Hitung rata-rata Z dari setiap bidang agar yang jauh digambar duluan
        sorted_faces = []
        for v_list, color, name in faces:
            avg_z = 0
            projected_pts = []
            for v in v_list:
                pt, z_depth = self.project(v[0], v[1], v[2])
                avg_z += z_depth
                projected_pts.append(pt)
            sorted_faces.append((avg_z / 4, projected_pts, color, name))
        
        # Urutkan dari yang paling jauh (Z besar) ke yang paling dekat (Z kecil)
        sorted_faces.sort(key=lambda x: x[0], reverse=True)

        for _, pts, color, name in sorted_faces:
            poly = QPolygonF(pts)
            self.scene.addPolygon(poly, QPen(QColor(80,80,80), 1), QBrush(color))
            
            if self.base_pixmap and name in ["front", "back", "spine"]:
                self._apply_texture(name, pts, w, h, t)

    def _apply_texture(self, name, dest_points, w, h, t):
        total_w_design = (w * 2) + t
        img_w, img_h = self.base_pixmap.width(), self.base_pixmap.height()
        sx = img_w / total_w_design
        sy = img_h / h

        # Crop area berdasarkan standar Full Spread: [Back] [Spine] [Front]
        if name == "back":
            rect = QRectF(0 * sx, 0, w * sx, h * sy)
        elif name == "spine":
            rect = QRectF(w * sx, 0, t * sx, h * sy)
        elif name == "front":
            rect = QRectF((w + t) * sx, 0, w * sx, h * sy)
        else: return

        cropped = self.base_pixmap.copy(rect.toRect())
        source_quad = QPolygonF([QPointF(0,0), QPointF(cropped.width(),0), 
                                 QPointF(cropped.width(),cropped.height()), QPointF(0,cropped.height())])
        
        trans = QTransform()
        if QTransform.quadToQuad(source_quad, QPolygonF(dest_points), trans):
            item = self.scene.addPixmap(cropped)
            item.setTransform(trans)
            item.setZValue(self.scene.items()[-1].zValue() + 0.1)

    def _load_raw_pixmap(self, path):
        if not path or path == "https://": return None
        pix = QPixmap()
        try:
            if path.startswith(("http://", "https://")):
                resp = requests.get(path, timeout=5); pix.loadFromData(resp.content)
            elif os.path.exists(path): pix.load(path)
            return pix if not pix.isNull() else None
        except: return None