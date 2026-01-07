from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView
from models.table.item_table_model import ItemTableModel

class DataTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.table = QTableView(self)
        self.model = ItemTableModel(self.table)

        self.table.setModel(self.model)

        # === TABLE BEHAVIOR ===
        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSortingEnabled(False)

        layout.addWidget(self.table)
