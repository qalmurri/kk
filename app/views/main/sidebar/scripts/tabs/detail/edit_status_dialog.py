from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel,
    QComboBox, QPushButton
)
from PySide6.QtCore import Signal

class EditStatusCoverDialog(QDialog):
    valueSaved = Signal(dict)

    def __init__(self, status_obj: dict, parent=None):
        super().__init__(parent)
        self.status_obj = status_obj

        self.setWindowTitle("Edit Status Cover")

        layout = QVBoxLayout(self)

        self.combo = QComboBox()
        self.combo.addItems(["Draft", "Proses", "Sudah"])  # nanti dari API

        current = status_obj["sectionstatus"]["name"]
        self.combo.setCurrentText(current)

        btn_save = QPushButton("Simpan")
        btn_save.clicked.connect(self.save)

        layout.addWidget(self.combo)
        layout.addWidget(btn_save)

    def save(self):
        new_value = self.combo.currentText()

        self.status_obj["sectionstatus"]["name"] = new_value

        self.valueSaved.emit(self.status_obj)
        self.accept()
