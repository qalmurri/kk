from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QToolBar
from PySide6.QtGui import QAction # Digunakan untuk membuat item di toolbar
from PySide6.QtCore import Qt
from .tabs import DataTab, CoverTab
from models.table.cover_table_model import CoverTableModel

class ScriptsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 1. Layout utama vertikal
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 2. TAMBAHKAN TOOLBAR (Area Tools)
        self.toolbar = QToolBar("Scripts Tools")
        self.toolbar.setMovable(False) # Agar toolbar tidak bisa digeser-geser
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) # Teks di samping icon

        # Contoh Tool 2: Export
        export_action = QAction("Export Data", self)
        export_action.triggered.connect(self.on_export_clicked)
        self.toolbar.addAction(export_action)

        # Tambahkan toolbar ke layout paling atas
        layout.addWidget(self.toolbar)

        # 3. Inisialisasi Tab Widget (Area Utama)
        self.shared_model = CoverTableModel(self)
        self.tabs = QTabWidget()
        self.tab_data = DataTab(model=self.shared_model, parent=self)
        self.tab_cover = CoverTab(model=self.shared_model, parent=self)


        self.tabs.addTab(self.tab_data, "Data")
        self.tabs.addTab(self.tab_cover, "Cover")
        
        layout.addWidget(self.tabs)

    def on_export_clicked(self):
        print("Mengekspor data ke file...")
