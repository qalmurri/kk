from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QSplitter, QMenu
from .widgets.cover_preview import CoverPreview
from PySide6.QtCore import Qt
from .detail.cover_window import CoverDetailWindow
from .base_persistent_table_tab import BasePersistentTableTab
from core.session import Session

class CoverTab(BasePersistentTableTab):
    TAB_KEY = "cover"
    VISIBLE_COLUMNS = {
        "id",
        "title",
        "status_cover",
        "process_desainer",
        # "cover.length",
        # "cover.height",
        # "cover.width",
        # "cover.x_axis",
        # "cover.y_axis",
        # "cover.zoom",
        # "cover.thumbnail",
    }

    def __init__(self, proxy, selection_model, parent=None):
        super().__init__(parent)

        self.proxy = proxy
        
        layout = QVBoxLayout(self)
        self.splitter = QSplitter(Qt.Horizontal)

        self.table = QTableView(self)
        self.table.setModel(proxy)
        self.table.setSelectionModel(selection_model)

        self.preview = CoverPreview(self)
        
        self.splitter.addWidget(self.table)
        self.splitter.addWidget(self.preview)
#        self.splitter.setSizes([400, 600])

        # Double Click
        self.table.doubleClicked.connect(self.on_double_click)

        # Right Click
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(self.splitter)

        self.apply_visible_columns()
        self.enable_column_persistence()
        # self._restore_column_sizes()
        # self._connect_column_resize()

        selection_model.selectionChanged.connect(
                self.on_selection_changed
                )

        self._restore_splitter_state()
        self.splitter.splitterMoved.connect(self._save_splitter_state)

        
    def on_selection_changed(self, selected, deselected):
        indexes = selected.indexes()
        if not indexes:
            return

        proxy_index = indexes[0]
        source_index = proxy_index.model().mapToSource(proxy_index)

        source_model = source_index.model()
        data = source_model._data[source_index.row()]

        self.current_data = data
        self.preview.update_preview(data) 

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
        
        dialog = CoverDetailWindow(self.current_data, self)
        dialog.exec()

    def apply_visible_columns(self):
        proxy = self.table.model()
        model = proxy.sourceModel()

        for col in range(model.columnCount()):
            self.table.setColumnHidden(col, True)

        for col in model.column_indexes_by_keys(self.VISIBLE_COLUMNS):
            self.table.setColumnHidden(col, False)

        for col in model.column_indexes_by_ids(self.VISIBLE_COLUMNS):
            self.table.setColumnHidden(col, False)

    def _restore_splitter_state(self):
        state = Session.get_splitter_state("cover_tab")
        if state:
            self.splitter.restoreState(state)
        else:
            self.splitter.setSizes([400, 600])

    def _save_splitter_state(self, pos, index):
        Session.set_splitter_state(
                "cover_tab",
                self.splitter.saveState()
                )
