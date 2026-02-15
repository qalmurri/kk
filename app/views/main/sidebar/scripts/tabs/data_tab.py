from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QMenu
from PySide6.QtCore import Qt
from .base_persistent_table_tab import BasePersistentTableTab
from .detail.data_window import DataDetailWindow

class DataTab(BasePersistentTableTab):
    TAB_KEY = "data"
    VISIBLE_COLUMNS = {
        "id",
        "title",
        "alias",
        "entry_date",
        "finish_date",
        "institute.name",
        "size.name",
        "process_desainer",
        "status_cover",
        "status_layouter",
        "status_isbn",
        "pembuat_layouter",
        "pemesan",

    }

    def __init__(self, proxy, selection_model, parent=None):
        super().__init__(parent)

        self.proxy = proxy

        layout = QVBoxLayout(self)
        self.table = QTableView(self)
        self.table.setModel(proxy)
        self.table.setSelectionModel(selection_model)

        self.table.doubleClicked.connect(self.on_double_click)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(self.table)

        self.enable_column_persistence()

        self.apply_visible_columns()

    def on_selection_changed(self, selected, deselected):
        pass

    def on_double_click(self, index):
        if not index.isValid():
            return

        self.open_detail_window()

    def on_right_click(self, pos):
        index = self.table.indexAt(pos)
        if not index.isValid():
            return

        menu = QMenu(self)

        detail_action = menu.addAction("Detail")
        action = menu.exec(self.table.viewport().mapToGlobal(pos))

        if action == detail_action:
            self.open_detail_window()

    def open_detail_window(self):
        dialog = DataDetailWindow(self)
        dialog.exec()

    def apply_visible_columns(self):
        proxy = self.table.model()
        model = proxy.sourceModel()

        # hide semua kolom
        for col in range(model.columnCount()):
            self.table.setColumnHidden(col, True)

        # show kolom yang diizinkan
        for col in model.column_indexes_by_keys(self.VISIBLE_COLUMNS):
            self.table.setColumnHidden(col, False)

        for col in model.column_indexes_by_ids(self.VISIBLE_COLUMNS):
            self.table.setColumnHidden(col, False)
