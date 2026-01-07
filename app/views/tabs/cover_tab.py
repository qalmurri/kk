from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QTableView,
    QSplitter
    )
from PySide6.QtCore import Qt


from models.table.cover_table_model import CoverTableModel
from views.tabs.widgets.cover_preview import CoverPreview

class CoverTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QHBoxLayout(self)
        
        # TABLE
        self.table = QTableView(self)
        self.model = CoverTableModel(self)

        self.table.setModel(self.model)
        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)

        # PREVIEW
        self.preview = CoverPreview(self)

        # SPLITTER
        splitter = QSplitter(Qt.Horizontal, self)
        splitter.addWidget(self.table)
        splitter.addWidget(self.preview)

        splitter.setSizes([300, 500])
        main_layout.addWidget(splitter)

        # SIGNAL
        self.table.selectionModel().selectionChanged.connect(
            self.on_row_selected
        )

    def on_row_selected(self, selected, deselected):
        if not selected.indexes():
            return
        
        row = selected.indexes()[0].row()
        data = self.model._data[row]

        self.preview.update_preview(data)
