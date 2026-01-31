from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView

class DataTab(QWidget):
    def __init__(self, proxy, selection_model, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.table = QTableView(self)
        self.table.setModel(proxy)
        self.table.setSelectionModel(selection_model)

        self.table.setColumnHidden(3, True)

        layout.addWidget(self.table)


class Data2Tab(QWidget):
    def __init__(self, proxy, selection_model, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.table = QTableView(self)
        self.table.setModel(proxy)
        self.table.setSelectionModel(selection_model)

        self.table.setColumnHidden(3, True)

        layout.addWidget(self.table)
