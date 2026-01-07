from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class CoverPreview(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.title = QLabel("No cover selected")
        self.title.setAlignment(Qt.AlignCenter)

        self.subtitle = QLabel("Preview area")
        self.subtitle.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(self.title)
        layout.addWidget(self.subtitle)
        layout.addStretch()

    def update_preview(self, cover_data: dict):
        self.title.setText(cover_data.get("title", "-"))
        self.subtitle.setText(f"Status: {cover_data.get('status', '-')}")
