from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QToolBar
from PySide6.QtGui import QAction # Digunakan untuk membuat item di toolbar
from PySide6.QtCore import Qt
from .tabs import DataTab, CoverTab
<<<<<<< HEAD

class ScriptsSidebar(QWidget):
=======
from models.table.cover_table_model import CoverTableModel

class ScriptsPage(QWidget):
>>>>>>> 6ec9f6e7845e0345b41b9d186459677b7ce1988d
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
<<<<<<< HEAD
        
        # Contoh Tool 1: Export
=======

        # Contoh Tool 2: Export
>>>>>>> 6ec9f6e7845e0345b41b9d186459677b7ce1988d
        export_action = QAction("Export Data", self)
        export_action.triggered.connect(self.on_export_clicked)
        self.toolbar.addAction(export_action)

        # Tambahkan toolbar ke layout paling atas
        layout.addWidget(self.toolbar)

        # 3. Inisialisasi Tab Widget (Area Utama)
<<<<<<< HEAD
        self.tabs = QTabWidget()
        self.tabs.addTab(DataTab(self), "Data")
        self.tabs.addTab(CoverTab(self), "Cover")
        
        layout.addWidget(self.tabs)

    # --- LOGIKA UNTUK TOOLS ---
    def on_refresh_clicked(self):
        print("Meresfresh data pada tab yang aktif...")
        # Contoh: akses tab saat ini
        current_tab = self.tabs.currentWidget()
        # if hasattr(current_tab, 'refresh_data'): current_tab.refresh_data()

    def on_export_clicked(self):
        print("Mengekspor data ke file...")
=======
        self.shared_model = CoverTableModel(self)
        self.tabs = QTabWidget()
        self.tab_data = DataTab(model=self.shared_model, parent=self)
        self.tab_cover = CoverTab(model=self.shared_model, parent=self)


        self.tabs.addTab(self.tab_data, "Data")
        self.tabs.addTab(self.tab_cover, "Cover")
        
        layout.addWidget(self.tabs)

    def on_export_clicked(self):
        print("Mengekspor data ke file...")
>>>>>>> 6ec9f6e7845e0345b41b9d186459677b7ce1988d
