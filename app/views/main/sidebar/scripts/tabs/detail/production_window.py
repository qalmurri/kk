from PySide6.QtWidgets import QDialog

class ProductionDetailWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail Production")
        self.resize (400, 300)
