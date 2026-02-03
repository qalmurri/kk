from PySide6.QtWidgets import QDialog

class IsbnDetailWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail Isbn")
        self.resize (400, 300)
