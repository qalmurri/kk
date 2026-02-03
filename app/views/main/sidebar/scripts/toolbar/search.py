from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QToolBar, QAbstractItemView, QDialog

class SearchData(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Search Data")
        self.resize (400, 300)