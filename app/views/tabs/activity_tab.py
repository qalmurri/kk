from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ActivityTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Activity content here"))