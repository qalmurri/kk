from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene
from views.tabs.widgets.graphics_view import InteractiveGraphicsView
from PySide6.QtGui import QPixmap, QBrush, QColor, QPen, QTransform, QPolygonF, QPainter
from PySide6.QtCore import Qt, QPointF, QRectF
import math, os, requests
from PySide6.QtOpenGLWidgets import QOpenGLWidget

class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.view = InteractiveGraphicsView()
# --- PERBAIKAN 1: GUNAKAN OPENGL UNTUK KUALITAS TAJAM ---
        self.view.setViewport(QOpenGLWidget()) 
        # -------------------------------------------------------
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QColor("#121212"))
        self.view.setScene(self.scene)
        self.view.setStyleSheet("background-color: #151515;")
        layout.addWidget(self.view)

        # Connect rotasi dari mouse di graphics_view
        self.view.rotationChanged.connect(self.update_rotation)
        
        # Default rotasi
        self.rot_x, self.rot_y = -20.0, -30.0
        self.last_cover_data = None
        self.base_pixmap = None

    def update_rotation(self, rx, ry):
        self.rot_x, self.rot_y = rx, ry
        self.render_scene()

    def update_preview(self, cover: dict = None):
        if cover:
            self.last_cover_data = cover
            self.base_pixmap = self._load_raw_pixmap(cover.get("thumbnail"))
        self.render_scene()

    def project(self, x, y, z):
        """Proyeksi 3D ke 2D dengan Rotasi XYZ"""
        rad_x, rad_y = math.radians(self.rot_x), math.radians(self.rot_y)
        # Rotasi Y
        nx = x * math.cos(rad_y) + z * math.sin(rad_y)
        nz = -x * math.sin(rad_y) + z * math.cos(rad_y)
        # Rotasi X
        ny = y * math.cos(rad_x) - nz * math.sin(rad_x)
        final_z = y * math.sin(rad_x) + nz * math.cos(rad_x)
        
        factor = 850 / (850 + final_z)
        return QPointF(nx * factor, ny * factor), final_z

    def render_scene(self):
        self.scene.clear()
        if not self.last_cover_data: return

        # Pengaturan Resolusi (Multiplier)
        # Ubah ke 2.0 atau 4.0 untuk hasil yang JAUH lebih tajam (Supersampling)
        q = 4.0 

        w = self.last_cover_data.get("width", 160)
        h = self.last_cover_data.get("height", 250)
        t = self.last_cover_data.get("length", 20)
        
        x_off = self.last_cover_data.get("x_axis", 0)
        y_off = self.last_cover_data.get("y_axis", 0)
        zoom = self.last_cover_data.get("zoom", 1.0)
        if zoom <= 0: zoom = 1.0

        cx, cy, cz = w/2, h/2, t/2

        # --- PERBAIKAN 2: MASTER CANVAS DENGAN RESOLUSI TINGGI ---
        total_w = (w * 2) + t
        # Kita kalikan ukuran kanvas dengan faktor kualitas 'q'
        master_canvas = QPixmap(int(total_w * q), int(h * q))
        master_canvas.fill(QColor("#ffffff"))

        if self.base_pixmap:
            painter = QPainter(master_canvas)
            # Aktifkan semua fitur penghalus
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            
            # Gambar thumbnail dengan skala yang sudah dikalikan multiplier
            tw = self.base_pixmap.width() * zoom * q
            th = self.base_pixmap.height() * zoom * q
            
            # Koordinat juga dikalikan multiplier
            dx = x_off * q
            dy = y_off * q
            
            painter.drawPixmap(QRectF(dx, dy, tw, th), self.base_pixmap, QRectF(self.base_pixmap.rect()))
            painter.end()

        # 2. DEFINISI BIDANG 3D
        # (Crop rect juga harus dikalikan dengan multiplier 'q')
        faces_def = [
            ([(0-cx,0-cy,0-cz), (w-cx,0-cy,0-cz), (w-cx,h-cy,0-cz), (0-cx,h-cy,0-cz)], "front", ((w+t)*q, 0, w*q, h*q)),
            ([(w-cx,0-cy,t-cz), (0-cx,0-cy,t-cz), (0-cx,h-cy,t-cz), (w-cx,h-cy,t-cz)], "back", (0, 0, w*q, h*q)),
            ([(0-cx,0-cy,t-cz), (0-cx,0-cy,0-cz), (0-cx,h-cy,0-cz), (0-cx,h-cy,t-cz)], "spine", (w*q, 0, t*q, h*q)),
            ([(w-cx,0-cy,0-cz), (w-cx,0-cy,t-cz), (w-cx,h-cy,t-cz), (w-cx,h-cy,0-cz)], "pages", None),
            ([(0-cx,0-cy,t-cz), (w-cx,0-cy,t-cz), (w-cx,0-cy,0-cz), (0-cx,0-cy,0-cz)], "top", None),
            ([(0-cx,h-cy,0-cz), (w-cx,h-cy,0-cz), (w-cx,h-cy,t-cz), (0-cx,h-cy,t-cz)], "bottom", None),
        ]

        # 3. PROYEKSI & SORTING
        rendered_faces = []
        for v_list, name, crop in faces_def:
            pts, sum_z = [], 0
            for v in v_list:
                p2d, z_d = self.project(v[0], v[1], v[2])
                pts.append(p2d); sum_z += z_d
            
            it = {"front":1.0, "top":0.9, "spine":0.7, "pages":0.6, "back":0.4, "bottom":0.3}.get(name, 1.0)
            color = QColor(int(255*it), int(255*it), int(255*it))
            rendered_faces.append((sum_z / 4, pts, color, name, crop))

        rendered_faces.sort(key=lambda x: x[0], reverse=True)

        # 4. DRAWING
        for _, pts, color, name, crop in rendered_faces:
            poly = QPolygonF(pts)
            self.scene.addPolygon(poly, QPen(color, 0.5), QBrush(color))

            if crop:
                # Potong bagian HD dari master_canvas
                section = master_canvas.copy(QRectF(*crop).toRect())
                self._apply_texture(section, pts)
            
            if name in ["pages", "top", "bottom"]:
                self._draw_paper_texture(pts, name, color)

    def _apply_texture(self, pix, dest_pts):
        source_quad = QPolygonF([QPointF(0,0), QPointF(pix.width(),0), 
                                 QPointF(pix.width(),pix.height()), QPointF(0,pix.height())])
        trans = QTransform()
        if QTransform.quadToQuad(source_quad, QPolygonF(dest_pts), trans):
            item = self.scene.addPixmap(pix)
            
            # --- PERBAIKAN 3: MODE TRANSFORMASI HALUS ---
            item.setTransformationMode(Qt.SmoothTransformation) 
            # ---------------------------------------------
            
            item.setTransform(trans)
            item.setZValue(self.scene.items()[-1].zValue() + 0.01)

    def _draw_paper_texture(self, pts, name, base_color):
        pen = QPen(base_color.darker(110), 0.4)
        for i in range(1, 10):
            t = i / 10
            if name == "pages":
                p1, p2 = pts[0] + (pts[3]-pts[0])*t, pts[1] + (pts[2]-pts[1])*t
            else:
                p1, p2 = pts[0] + (pts[1]-pts[0])*t, pts[3] + (pts[2]-pts[3])*t
            self.scene.addLine(p1.x(), p1.y(), p2.x(), p2.y(), pen)

    def _load_raw_pixmap(self, path):
        if not path or path == "https://": return None
        pix = QPixmap()
        try:
            if path.startswith(("http", "https")):
                r = requests.get(path, timeout=5); pix.loadFromData(r.content)
            elif os.path.exists(path):
                pix.load(path)
            return pix if not pix.isNull() else None
        except: return None