from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QGroupBox, QPushButton, QGridLayout
)
from PySide6.QtCore import Qt

class BerandaPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)

        # ===================== JUDUL =====================
        title = QLabel("Beranda")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        main_layout.addWidget(title)

        # ===================== STATUS SISTEM =====================
        status_box = QGroupBox("Status Sistem")
        status_layout = QGridLayout(status_box)

        status_layout.addWidget(QLabel("Server:"), 0, 0)
        status_layout.addWidget(QLabel("🟢 Terhubung"), 0, 1)

        status_layout.addWidget(QLabel("User:"), 1, 0)
        status_layout.addWidget(QLabel("Qalmurri"), 1, 1)

        status_layout.addWidget(QLabel("Last Sync:"), 2, 0)
        status_layout.addWidget(QLabel("2 menit lalu"), 2, 1)

        main_layout.addWidget(status_box)

        # ===================== RINGKASAN DATA =====================
        summary_box = QGroupBox("Ringkasan")
        summary_layout = QHBoxLayout(summary_box)
        summary_layout.setSpacing(24)

        summary_layout.addWidget(self._build_summary_card("Total Cover", "120"))
        summary_layout.addWidget(self._build_summary_card("Dalam Produksi", "32"))
        summary_layout.addWidget(self._build_summary_card("Draft", "14"))
        summary_layout.addWidget(self._build_summary_card("Perlu Review", "8"))

        main_layout.addWidget(summary_box)

        # ===================== AKSI CEPAT =====================
        action_box = QGroupBox("Aksi Cepat")
        action_layout = QHBoxLayout(action_box)
        action_layout.setSpacing(12)

        btn_add = QPushButton("➕ Tambah Data")
        btn_refresh = QPushButton("🔄 Refresh")
        btn_export = QPushButton("📤 Export")
        btn_setting = QPushButton("⚙️ Pengaturan")

        for btn in (btn_add, btn_refresh, btn_export, btn_setting):
            btn.setFixedHeight(36)
            action_layout.addWidget(btn)

        action_layout.addStretch()
        main_layout.addWidget(action_box)

        main_layout.addStretch()

    # ===================== HELPER =====================
    def _build_summary_card(self, title: str, value: str) -> QWidget:
        card = QGroupBox()
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignCenter)

        lbl_value = QLabel(value)
        lbl_value.setStyleSheet("font-size: 22px; font-weight: bold;")

        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("color: gray;")

        layout.addWidget(lbl_value)
        layout.addWidget(lbl_title)

        card.setFixedWidth(150)
        return card
