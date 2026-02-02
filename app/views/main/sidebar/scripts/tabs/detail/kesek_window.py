from PySide6.QtWidgets import QDialog

class KesekDetailWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail Kesek")
        self.resize (400, 300)
