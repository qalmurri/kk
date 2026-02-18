from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QToolBar, QAbstractItemView, QDialog
from PySide6.QtCore import QSortFilterProxyModel, Qt, QItemSelectionModel
from PySide6.QtGui import QAction

class ChartPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)