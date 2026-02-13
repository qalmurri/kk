from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class EditFieldDialog(QDialog):
    def __init__(self, field_name: str, value="", parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Edit {field_name}")
        self.resize(300, 120)

        self.input = QLineEdit(str(value))

        btn_save = QPushButton("Simpan")
        btn_cancel = QPushButton("Batal")

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(field_name))
        layout.addWidget(self.input)
        layout.addWidget(btn_save)
        layout.addWidget(btn_cancel)

        btn_save.clicked.connect(self.accept)
        btn_cancel.clicked.connect(self.reject)

    def get_value(self):
        return self.input.text()