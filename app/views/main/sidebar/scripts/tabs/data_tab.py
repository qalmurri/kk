from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView

class DataTab(QWidget):
    def __init__(self, proxy, selection_model, parent=None): # Terima model dari parent
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.table = QTableView(self)
        self.table.setModel(proxy) # Gunakan model bersama
        self.table.setSelectionModel(selection_model)

        self.table.setColumnHidden(3, True)

        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)
