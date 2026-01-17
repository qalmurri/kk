from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView

class DataTab(QWidget):
    def __init__(self, model, parent=None): # Terima model dari parent
        super().__init__(parent)
        layout = QVBoxLayout(self)

        # buar proxy model
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(model)
        
        self.table = QTableView(self)
        self.table.setModel(self.proxy_model) # Gunakan model bersama

        self.table.setSortingEnabled(True)

        self.table.setColumnHidden(3, True)

        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)
