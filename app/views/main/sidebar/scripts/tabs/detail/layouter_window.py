from PySide6.QtWidgets import QDialog

class LayouterDetailWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail Layouter")
        self.resize (400, 300)
