from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Signal


class EditableRow(QWidget):
    editRequested = Signal()

    def __init__(self, label_text: str, parent=None):
        super().__init__(parent)

        self.label = QLabel(label_text)
        self.value = QLabel("-")
        self.edit_btn = QPushButton("Edit")
        self.edit_btn.setFixedWidth(60)

        layout = QHBoxLayout(self)
        layout.addWidget(self.label, 1)
        layout.addWidget(self.value, 2)
        layout.addWidget(self.edit_btn)
        layout.setContentsMargins(0, 0, 0, 0)

        self.edit_btn.clicked.connect(self.editRequested.emit)

    def set_value(self, text):
        self.value.setText(str(text))
