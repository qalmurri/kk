from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QMenu
from PySide6.QtCore import Qt
from .base_persistent_table_tab import BasePersistentTableTab
from .detail.isbn_window import IsbnDetailWindow

class IsbnTab(BasePersistentTableTab):
    TAB_KEY = "isbn"
    VISIBLE_COLUMNS = {
        "id",
        "title",
        "status_isbn",
        "isbn",
        "eisbn",
        }

    def __init__(self, proxy, selection_model, parent=None):
        super().__init__(parent)

        self.proxy = proxy

        layout = QVBoxLayout(self)
        self.table = QTableView(self)
        self.table.setModel(proxy)
        self.table.setSelectionModel(selection_model)

        # Double Click
        self.table.doubleClicked.connect(self.on_double_click)

        # Right Click
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(self.table)

        self.enable_column_persistence()
        self.apply_visible_columns()

        selection_model.selectionChanged.connect(
                self.on_selection_changed
        )

    def on_selection_changed(self, selected, deselected):
        indexes = selected.indexes()
        if not indexes:
            return

        proxy_index = indexes[0]
        source_index = proxy_index.model().mapToSource(proxy_index)

        source_model = source_index.model()
        data = source_model._data[source_index.row()]

        self.current_data = data

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
        if not hasattr(self, "current_data") or not self.current_data:
            return 

        dialog = IsbnDetailWindow(self.current_data, self)
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
