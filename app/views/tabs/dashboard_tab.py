from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class DashboardTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Dashboard content here"))