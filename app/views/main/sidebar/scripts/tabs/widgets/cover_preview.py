from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene
from .graphics_view import InteractiveGraphicsView
from PySide6.QtGui import QPixmap, QBrush, QColor, QPen, QTransform, QPolygonF, QPainter
from PySide6.QtCore import Qt, QPointF, QRectF
from PySide6.QtOpenGLWidgets import QOpenGLWidget
import math, os, requests

class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.view = InteractiveGraphicsView()
        
        # Gunakan OpenGL untuk performa dan ketajaman
        self.view.setViewport(QOpenGLWidget()) 
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QColor("#121212"))
        self.view.setScene(self.scene)
        layout.addWidget(self.view)

        self.view.rotationChanged.connect(self.update_rotation)
        self.rot_x, self.rot_y = -20.0, -30.0
        self.last_cover_data = None
        self.base_pixmap = None

# --- LOAD GAMBAR KERTAS PUTIH ---
        # Pastikan file ini ada di folder proyek Anda
        self.paper_pixmap = QPixmap("white_paper.jpg")

    def update_rotation(self, rx, ry):
        self.rot_x, self.rot_y = rx, ry
        self.render_scene()

    def update_preview(self, cover: dict = None):
        if cover:
            self.last_cover_data = cover
            self.base_pixmap = self._load_raw_pixmap(cover.get("thumbnail"))
        self.render_scene()

    def project(self, x, y, z):
        rad_x, rad_y = math.radians(self.rot_x), math.radians(self.rot_y)
        nx = x * math.cos(rad_y) + z * math.sin(rad_y)
        nz = -x * math.sin(rad_y) + z * math.cos(rad_y)
        ny = y * math.cos(rad_x) - nz * math.sin(rad_x)
        fz = y * math.sin(rad_x) + nz * math.cos(rad_x)
        factor = 850 / (850 + fz)
        return QPointF(nx * factor, ny * factor), fz

    def render_scene(self):
        self.scene.clear()
        if not self.last_cover_data: return

        q = 4.0 # High Quality Multiplier
        w = self.last_cover_data.get("width", 160)
        h = self.last_cover_data.get("height", 250)
        t = self.last_cover_data.get("length", 20)
        x_off, y_off = self.last_cover_data.get("x_axis", 0), self.last_cover_data.get("y_axis", 0)
        zoom = self.last_cover_data.get("zoom", 1.0)
        if zoom <= 0: zoom = 1.0

        cx, cy, cz = w/2, h/2, t/2

        # 1. MASTER CANVAS (Manual Placement)
        total_w = (w * 2) + t
        master_canvas = QPixmap(int(total_w * q), int(h * q))
        master_canvas.fill(Qt.white)

        if self.base_pixmap:
            painter = QPainter(master_canvas)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            tw, th = self.base_pixmap.width() * zoom * q, self.base_pixmap.height() * zoom * q
            painter.drawPixmap(QRectF(x_off * q, y_off * q, tw, th), self.base_pixmap, QRectF(self.base_pixmap.rect()))
            painter.end()

        # 2. DEFINISI 6 SISI BOX
        faces_def = [
            ([(0-cx,0-cy,0-cz), (w-cx,0-cy,0-cz), (w-cx,h-cy,0-cz), (0-cx,h-cy,0-cz)], "front", ((w+t)*q, 0, w*q, h*q)),
            ([(w-cx,0-cy,t-cz), (0-cx,0-cy,t-cz), (0-cx,h-cy,t-cz), (w-cx,h-cy,t-cz)], "back", (0, 0, w*q, h*q)),
            ([(0-cx,0-cy,t-cz), (0-cx,0-cy,0-cz), (0-cx,h-cy,0-cz), (0-cx,h-cy,t-cz)], "spine", (w*q, 0, t*q, h*q)),
            ([(w-cx,0-cy,0-cz), (w-cx,0-cy,t-cz), (w-cx,h-cy,t-cz), (w-cx,h-cy,0-cz)], "pages", None),
            ([(0-cx,0-cy,t-cz), (w-cx,0-cy,t-cz), (w-cx,0-cy,0-cz), (0-cx,0-cy,0-cz)], "top", None),
            ([(0-cx,h-cy,0-cz), (w-cx,h-cy,0-cz), (w-cx,h-cy,t-cz), (0-cx,h-cy,t-cz)], "bottom", None),
        ]

        # 3. PROYEKSI & SORTING
        rendered = []
        for v_list, name, crop in faces_def:
            pts, sum_z = [], 0
            for v in v_list:
                p, z = self.project(v[0], v[1], v[2])
                pts.append(p); sum_z += z
            
            it = {"front":1.0, "top":0.9, "spine":0.7, "pages":0.6, "back":0.4, "bottom":0.3}.get(name, 1.0)
            color = QColor(int(255*it), int(255*it), int(255*it))
            rendered.append((sum_z / 4, pts, color, crop))

        rendered.sort(key=lambda x: x[0], reverse=True)

        # 4. DRAWING
        for _, pts, color, crop in rendered:
            poly = QPolygonF(pts)
            self.scene.addPolygon(poly, QPen(color, 0.5), QBrush(color))
            
            # --- LOGIKA PENEMPELAN TEKSTUR ---
            if crop:
                # Sisi sampul (front, back, spine)
                section = master_canvas.copy(QRectF(*crop).toRect())
                self._apply_texture(section, pts)
            else:
                # Sisi yang None (pages, top, bottom) diganti gambar putih
                if not self.paper_pixmap.isNull():
                    self._apply_texture(self.paper_pixmap, pts)

    def _apply_texture(self, pix, dest_pts):
        source_quad = QPolygonF([QPointF(0,0), QPointF(pix.width(),0), QPointF(pix.width(),pix.height()), QPointF(0,pix.height())])
        trans = QTransform()
        if QTransform.quadToQuad(source_quad, QPolygonF(dest_pts), trans):
            item = self.scene.addPixmap(pix)
            item.setTransformationMode(Qt.SmoothTransformation)
            item.setTransform(trans)
            item.setZValue(self.scene.items()[-1].zValue() + 0.01)

    def _load_raw_pixmap(self, path):
        if not path or path == "https://": return None
        pix = QPixmap()
        try:
            if path.startswith(("http", "https")):
                r = requests.get(path, timeout=5); pix.loadFromData(r.content)
            else: pix.load(path)
            return pix if not pix.isNull() else None
        except: return None
