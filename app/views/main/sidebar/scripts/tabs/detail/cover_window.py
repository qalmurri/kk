# from PySide6.QtWidgets import QDialog
# 
# class CoverDetailWindow(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Detail Cover")
#         self.resize (400, 300)

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QTabWidget, QWidget,
    QGroupBox, QFormLayout, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt
from .edit_field_dialog import EditFieldDialog
from .widgets.editable_row import EditableRow
from PySide6.QtWidgets import QSplitter, QListWidget

class CoverDetailWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Detail Cover")
        self.resize(600, 450)

        main_layout = QVBoxLayout(self)

        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # KIRI : Tabs
        self.tabs = QTabWidget()
        splitter.addWidget(self.tabs)

        # KANAN : Riwayat Edit
        history_box = QGroupBox("Riwayat Edit")
        history_layout = QVBoxLayout(history_box)

        self.history_list = QListWidget()
        history_layout.addWidget(self.history_list)
        self.history_list.addItem("Belum ada riwayat perubahan")

        splitter.addWidget(history_box)

        # ukuran awal (optional tapi enak)
        splitter.setSizes([450, 200])

        self._build_general_tab()
        self._build_size_tab()
        self._build_transform_tab()
        self._build_preview_tab()

    # -------------------- TAB 1 : GENERAL --------------------
    def _build_general_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        group_info = QGroupBox("Informasi Umum")
        form = QFormLayout(group_info)
        form.addRow("ID:", QLabel("-"))
        form.addRow("Judul:", QLabel("-"))
        form.addRow("Desainer:", QLabel("-"))

        group_status = QGroupBox("Status")
        form_status = QFormLayout(group_status)
        form_status.addRow("Status Cover:", QLabel("-"))
        form_status.addRow("Proses Desainer:", QLabel("-"))

        layout.addWidget(group_info)
        layout.addWidget(group_status)
        layout.addStretch()

        self.tabs.addTab(tab, "General")

    # -------------------- TAB 2 : SIZE --------------------
    def _build_size_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        group = QGroupBox("Dimensi Cover")
        vbox = QVBoxLayout(group)

        self.row_width = EditableRow("Width")
        self.row_height = EditableRow("Height")
        self.row_thickness = EditableRow("Thickness")

        self.row_width.editRequested.connect(
            lambda: self.open_edit_dialog("Width", self.row_width)
        )
        self.row_height.editRequested.connect(
            lambda: self.open_edit_dialog("Height", self.row_height)
        )
        self.row_thickness.editRequested.connect(
            lambda: self.open_edit_dialog("Thickness", self.row_thickness)
        )

        vbox.addWidget(self.row_width)
        vbox.addWidget(self.row_height)
        vbox.addWidget(self.row_thickness)

        layout.addWidget(group)
        layout.addStretch()
        self.tabs.addTab(tab, "Cover Size")

    # -------------------- TAB 3 : TRANSFORM --------------------
    def _build_transform_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        group_transform = QGroupBox("Transformasi")
        form = QFormLayout(group_transform)
        form.addRow("X Axis:", QLabel("-"))
        form.addRow("Y Axis:", QLabel("-"))
        form.addRow("Zoom:", QLabel("-"))

        layout.addWidget(group_transform)
        layout.addStretch()

        self.tabs.addTab(tab, "Position & Zoom")

    # -------------------- TAB 4 : PREVIEW --------------------
    def _build_preview_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        group_file = QGroupBox("File & Thumbnail")
        form = QFormLayout(group_file)
        form.addRow("Thumbnail:", QLabel("-"))
        form.addRow("File Path:", QLabel("-"))

        layout.addWidget(group_file)
        layout.addStretch()

        self.tabs.addTab(tab, "Preview Info")

    def open_edit_dialog(self, field_name, row_widget):
        dialog = EditFieldDialog(
            field_name,
            row_widget.value.text(),
            self
        )
        if dialog.exec():
            row_widget.set_value(dialog.get_value())