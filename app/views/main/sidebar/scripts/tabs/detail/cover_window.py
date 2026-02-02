from PySide6.QtWidgets import QDialog

class CoverDetailWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail Cover")
        self.resize (400, 300)
