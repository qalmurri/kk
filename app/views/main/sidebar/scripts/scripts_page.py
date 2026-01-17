from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from .tabs import CoverTab, DataTab

class ScriptsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Layout utama halaman Scripts
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Inisialisasi Tab Widget
        self.tabs = QTabWidget()
        self.tabs.addTab(DataTab(self), "Data")
        self.tabs.addTab(CoverTab(self), "Cover")
        
        # Masukkan tabs ke dalam layout halaman
        layout.addWidget(self.tabs)
