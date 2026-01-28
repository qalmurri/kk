from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QToolBar
from PySide6.QtGui import QAction
from PySide6.QtCore import QSortFilterProxyModel, Qt, QItemSelectionModel
from .tabs import DataTab, CoverTab
from models.table.item_table_model import DataTableModel

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

        searching_action = QAction("search", self)
        searching_action.triggered.connect(self.on_search_clicked)
        self.toolbar.addAction(searching_action)

        # Tambahkan toolbar ke layout paling atas
        layout.addWidget(self.toolbar)

        # # 3. Inisialisasi Tab Widget (Area Utama)
        # self.shared_model = DataTableModel(self)
        # self.tabs = QTabWidget()
        # self.tab_data = DataTab(model=self.shared_model, parent=self)
        # self.tab_cover = CoverTab(model=self.shared_model, parent=self)


        # self.tabs.addTab(self.tab_data, "Data")
        # self.tabs.addTab(self.tab_cover, "Cover")
        # 
        # layout.addWidget(self.tabs)

        # SHARED SOURCE MODEL
        self.shared_model = DataTableModel(self)

        # satu proxy
        self.shared_proxy = QSortFilterProxyModel(self)
        self.shared_proxy.setSourceModel(self.shared_model)

        # SHARED SELECTION MODEL (INI KUNCI)
        self.shared_selection = QItemSelectionModel(self.shared_proxy)

        self.tabs = QTabWidget()

        self.tab_data = DataTab(
            proxy=self.shared_proxy,
            selection_model=self.shared_selection,
            parent=self
        )

        self.tab_cover = CoverTab(
            proxy=self.shared_proxy,
            selection_model=self.shared_selection,
            parent=self
        )

        self.tabs.addTab(self.tab_data, "Data")
        self.tabs.addTab(self.tab_cover, "Cover")

        layout.addWidget(self.tabs)

    def on_export_clicked(self):
        print("Mengekspor data ke file...")

    def on_search_clicked(self):
        print("Searhing")
