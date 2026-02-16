from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QWidget, QHBoxLayout,
    QGroupBox, QFormLayout, QLabel,
    QSplitter, QListWidget, QPushButton,
    QTabWidget
)
from PySide6.QtCore import Qt

class DataDetailWindow(QDialog):
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)

        self.data = data

        self.setWindowTitle("Detail Data")
        self.resize(720, 480)

        main_layout = QVBoxLayout(self)

        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # ===================== KIRI : TABS =====================
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        self.tabs = QTabWidget()
        self.tabs.addTab(self._build_general_tab(), "Informasi Umum")
        self.tabs.addTab(self._build_status_tab(), "Status")

        left_layout.addWidget(self.tabs)
        splitter.addWidget(left_panel)

        # ===================== KANAN : RIWAYAT =====================
        history_box = QGroupBox("Riwayat Edit")
        history_layout = QVBoxLayout(history_box)

        self.history_list = QListWidget()
        self.history_list.addItem("Belum ada riwayat perubahan")
        history_layout.addWidget(self.history_list)

        splitter.addWidget(history_box)

        splitter.setSizes([500, 220])

    # ==========================================================
    # TAB : INFORMASI UMUM
    # ==========================================================
    def _build_general_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        group_info = QGroupBox("Detail")
        form = QFormLayout(group_info)

        form.addRow("Judul:", self._info_row(self.data.get("title", "-")))
        form.addRow("Alias:", self._info_row("-"))
        form.addRow("Entry Date:", self._info_row("-"))
        form.addRow("Finish Date:", self._info_row("-"))
        form.addRow("Institute:", self._info_row("-"))
        form.addRow("Size:", self._info_row("-"))
        form.addRow("Desainer:", self._info_row("-"))
        form.addRow("Layouter:", self._info_row("-"))
        form.addRow("Status:", self._info_row("-"))
        form.addRow("Order:", self._info_row("-"))

        layout.addWidget(group_info)
        layout.addStretch()
        return tab

    def _build_status_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        group_status = QGroupBox("Status Cover")
        form = QFormLayout(group_status)

        status_obj = self.get_status_cover()
        status_name = "-"

        if status_obj:
            status_name = status_obj.get("sectionstatus", {}).get("name", "-")

        self.lbl_status_cover = QLabel(status_name)

        btn_edit = QPushButton("Edit")
        btn_edit.setFixedWidth(70)
        btn_edit.setEnabled(False)
        btn_edit.setToolTip("Fitur edit belum tersedia")

        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.addWidget(self.lbl_status_cover)
        row_layout.addStretch()
        row_layout.addWidget(btn_edit)

        form.addRow("Status:", row_widget)

        layout.addWidget(group_status)
        layout.addStretch()
        return tab

    def _info_row(self, value: str):
        label = QLabel(value)

        btn_edit = QPushButton("Edit")
        btn_edit.setFixedWidth(60)
        btn_edit.setEnabled(False)
        btn_edit.setToolTip("Fitur edit belum tersedia")

        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.addWidget(label)
        row_layout.addStretch()
        row_layout.addWidget(btn_edit)

        return row_widget

    def get_status_cover(self):
        statuses = self.data.get("status", [])

        for s in statuses:
            label = s.get("labelstatus", {}).get("name")
            if label == "Desainer":
                return s

        return None
