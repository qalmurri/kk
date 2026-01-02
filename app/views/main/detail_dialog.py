from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QTextEdit, QTabWidget
)
import json

class DetailDialog(QDialog):
    def __init__(self, raw_data: dict, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detail Script")
        self.resize(600, 500)

        tabs = QTabWidget()

        # Tab 1: Info Umum
        info_tab = QVBoxLayout()
        info_tab.addWidget(QLabel(f"Judul: {raw_data.get('title')}"))
        info_tab.addWidget(QLabel(
            f"Fakultas: {raw_data.get('institute', {}).get('name')}"
        ))

        info_widget = QDialog()
        info_widget.setLayout(info_tab)

        # Tab 2: Raw JSON (debug / dev)
        raw_tab = QTextEdit()
        raw_tab.setReadOnly(True)
        raw_tab.setText(json.dumps(raw_data, indent=2, ensure_ascii=False))

        tabs.addTab(info_widget, "Info")
        tabs.addTab(raw_tab, "Raw JSON")

        layout = QVBoxLayout(self)
        layout.addWidget(tabs)
