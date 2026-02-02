from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QSplitter, QMenu
from .widgets.cover_preview import CoverPreview
from PySide6.QtCore import Qt
from .detail.cover_window import CoverDetailWindow

class CoverTab(QWidget):
    def __init__(self, proxy, selection_model, parent=None):
        super().__init__(parent)

        self.proxy = proxy
        
        layout = QVBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)

        self.table = QTableView(self)
        self.table.setModel(proxy)
        self.table.setSelectionModel(selection_model)

        self.preview = CoverPreview(self)
        
        splitter.addWidget(self.table)
        splitter.addWidget(self.preview)
        splitter.setSizes([400, 600])

        # Double Click
        self.table.doubleClicked.connect(self.on_double_click)

        # Right Click
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(splitter)

        selection_model.selectionChanged.connect(
                self.on_selection_changed
                )

        self.table.setColumnHidden(2, True)
        self.table.setColumnHidden(3, True)
        self.table.setColumnHidden(4, True)
        self.table.setColumnHidden(5, True)
        
    def on_selection_changed(self, selected, deselected):
        indexes = selected.indexes()
        if not indexes:
            return
        proxy_index = indexes[0]
        source_index = proxy_index.model().mapToSource(proxy_index)

        source_model = source_index.model()
        data = source_model._data[source_index.row()]

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
        dialog = CoverDetailWindow(self)
        dialog.exec()
