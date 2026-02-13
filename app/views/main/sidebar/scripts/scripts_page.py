from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QToolBar, QAbstractItemView, QDialog
from PySide6.QtCore import QSortFilterProxyModel, Qt, QItemSelectionModel
from PySide6.QtGui import QAction

from network.data_service import fetch_scripts
from models.table.item_table_model import DataTableModel
from .tabs import (
    DataTab,
    ProductionTab,
    CoverTab,
    LayouterTab,
    IsbnTab
)
from .toolbar.search import SearchData
from core.session import Session

class ScriptsPage(QWidget):
    def load_data(self):
        params = {
            "fields": "id,title,alias,is_active,entry_date,finish_date,institute,size",
            "include": "orderers,status,flag,identification,process,cover"
        }

        data = fetch_scripts(params)

        self.shared_model.set_api_data(data)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.toolbar = QToolBar("Scripts Tools")
        self.toolbar.setMovable(False)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) # Teks di samping icon

        export_action = QAction("Export Data", self)
        export_action.triggered.connect(self.on_export_clicked)
        self.toolbar.addAction(export_action)

        refresh_action = QAction("Refresh", self)
        refresh_action.triggered.connect(self.on_refresh_clicked)
        self.toolbar.addAction(refresh_action)

        searching_action = QAction("Search", self)
        searching_action.triggered.connect(self.on_search_clicked)
        self.toolbar.addAction(searching_action)

        layout.addWidget(self.toolbar)
        self.shared_model = DataTableModel(self)

        self.shared_proxy = QSortFilterProxyModel(self)
        self.shared_proxy.setSourceModel(self.shared_model)

        self.shared_selection = QItemSelectionModel(self.shared_proxy)

        self.tabs = QTabWidget()

        self.tab_data = DataTab(
            proxy=self.shared_proxy,
            selection_model=self.shared_selection,
            parent=self
        )
        
        self.tab_production = ProductionTab(
            proxy=self.shared_proxy,
            selection_model=self.shared_selection,
            parent=self
        )
        
        self.tab_layouter = LayouterTab(
            proxy=self.shared_proxy,
            selection_model=self.shared_selection,
            parent=self
        )

        self.tab_isbn = IsbnTab(
            proxy=self.shared_proxy,
            selection_model=self.shared_selection,
            parent=self
        )

        self.tab_cover = CoverTab( proxy=self.shared_proxy,
            selection_model=self.shared_selection,
            parent=self
        )

        self._apply_global_table_settings(self.tab_data.table)
        self._apply_global_table_settings(self.tab_production.table)
        self._apply_global_table_settings(self.tab_cover.table)
        self._apply_global_table_settings(self.tab_isbn.table)
        self._apply_global_table_settings(self.tab_layouter.table)

        self.tabs.addTab(self.tab_data, "Data")
        self.tabs.addTab(self.tab_cover, "Cover")
        self.tabs.addTab(self.tab_layouter, "Layouter")
        self.tabs.addTab(self.tab_isbn, "Isbn")
        self.tabs.addTab(self.tab_production, "Production")

        last_tab = Session.get_scripts_last_tab()
        self.tabs.setCurrentIndex(last_tab)

        self.tabs.currentChanged.connect(self.on_tab_changed)

        layout.addWidget(self.tabs)
        self.load_data()

    def _apply_global_table_settings(self, table: QAbstractItemView):
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.horizontalHeader().setStretchLastSection(True)

    def on_export_clicked(self):
        print("Export")

    def on_search_clicked(self):
        dialog = SearchData(self)
        dialog.exec()

    def on_refresh_clicked(self):
        print("Refresh")

    def on_tab_changed(self, index: int):
        Session.set_scripts_last_tab(index)
