from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QSplitter
from .widgets.cover_preview import CoverPreview
from PySide6.QtCore import Qt

class CoverTab(QWidget):
    def __init__(self, proxy, selection_model, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)

        self.table = QTableView(self)
        self.table.setModel(proxy)
        self.table.setSelectionModel(selection_model)

        self.preview = CoverPreview(self)
        
        splitter.addWidget(self.table)
        splitter.addWidget(self.preview)
        splitter.setSizes([400, 600]) # Atur proporsi awal
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
