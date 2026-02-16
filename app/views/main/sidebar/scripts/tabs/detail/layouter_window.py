from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QWidget, QHBoxLayout,
    QGroupBox, QFormLayout, QLabel,
    QSplitter, QListWidget, QPushButton, QCheckBox
)
from PySide6.QtCore import Qt


class LayouterDetailWindow(QDialog):
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)

        self.data = data

        self.setWindowTitle("Detail Layouter")
        self.resize(600, 450)

        main_layout = QVBoxLayout(self)

        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # ===================== KIRI : DETAIL =====================
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        self._build_general_section(left_layout)

        left_layout.addStretch()
        splitter.addWidget(left_panel)

        # ===================== KANAN : RIWAYAT =====================
        history_box = QGroupBox("Riwayat Edit")
        history_layout = QVBoxLayout(history_box)

        self.history_list = QListWidget()
        self.history_list.addItem("Belum ada riwayat perubahan")
        history_layout.addWidget(self.history_list)

        splitter.addWidget(history_box)

        splitter.setSizes([420, 180])

    # ==========================================================
    # GENERAL SECTION
    # ==========================================================
    def _build_general_section(self, parent_layout):
        group_info = QGroupBox("Informasi Umum")
        form = QFormLayout(group_info)

        form.addRow("Judul:", QLabel(self.data.get("title", "-")))
        form.addRow("Size:", QLabel("-"))

        # ---------- BOOLEAN CHECKLIST ----------
        form.addRow("Layouter:", self._boolean_row(False))
        form.addRow("File:", self._boolean_row(False))
        form.addRow("Photo:", self._boolean_row(False))
        form.addRow("CV:", self._boolean_row(False))
        form.addRow("Sinopsis:", self._boolean_row(False))
        form.addRow("Editor:", self._boolean_row(False))
        form.addRow("Kata Pengantar:", self._boolean_row(False))
        form.addRow("Daftar Pustaka:", self._boolean_row(False))

        parent_layout.addWidget(group_info)

        # ---------- STATUS ----------
        group_status = QGroupBox("Status")
        form_status = QFormLayout(group_status)

        status_obj = self.get_status_cover()
        status_name = "-"

        if status_obj:
            status_name = status_obj.get("sectionstatus", {}).get("name", "-")

        self.lbl_status_cover = QLabel(status_name)

        btn_edit_status = QPushButton("Edit")
        btn_edit_status.setFixedWidth(60)
        btn_edit_status.setEnabled(False)
        btn_edit_status.setToolTip("Edit status akan tersedia")

        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.addWidget(self.lbl_status_cover)
        row_layout.addStretch()
        row_layout.addWidget(btn_edit_status)

        form_status.addRow("Status Cover:", row_widget)
        parent_layout.addWidget(group_status)

    # ==========================================================
    # HELPER BOOLEAN ROW
    # ==========================================================
    def _boolean_row(self, checked: bool):
        """
        Row boolean:
        kiri  : label (-)
        kanan : checkbox (disabled)
        """
        label = QLabel("-")

        checkbox = QCheckBox()
        checkbox.setChecked(checked)
        checkbox.setEnabled(False)
        checkbox.setToolTip("Readonly")

        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.addWidget(label)
        row_layout.addStretch()
        row_layout.addWidget(checkbox)

        return row_widget

    # ==========================================================
    # GET STATUS
    # ==========================================================
    def get_status_cover(self):
        statuses = self.data.get("status", [])

        for s in statuses:
            label = s.get("labelstatus", {}).get("name")
            if label == "Desainer":
                return s

        return None
