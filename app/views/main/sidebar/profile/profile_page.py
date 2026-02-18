from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QGroupBox, QPushButton, QFormLayout
)
from PySide6.QtCore import Qt


class ProfilePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)

        # ===================== HEADER =====================
        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)

        avatar = QLabel("👤")
        avatar.setFixedSize(64, 64)
        avatar.setAlignment(Qt.AlignCenter)
        avatar.setStyleSheet(
            "font-size: 32px;"
            "border: 1px solid #ccc;"
            "border-radius: 32px;"
        )

        user_info = QVBoxLayout()
        lbl_name = QLabel("Qalmurri")
        lbl_name.setStyleSheet("font-size: 18px; font-weight: bold;")
        lbl_role = QLabel("Desainer")
        lbl_role.setStyleSheet("color: gray;")

        user_info.addWidget(lbl_name)
        user_info.addWidget(lbl_role)

        header_layout.addWidget(avatar)
        header_layout.addSpacing(12)
        header_layout.addLayout(user_info)
        header_layout.addStretch()

        main_layout.addWidget(header)

        # ===================== INFORMASI AKUN =====================
        account_box = QGroupBox("Informasi Akun")
        account_form = QFormLayout(account_box)

        account_form.addRow("Username:", QLabel("qalmurri"))
        account_form.addRow("Email:", QLabel("qalmurri@email.com"))
        account_form.addRow("Role:", QLabel("Desainer"))
        account_form.addRow("Status:", QLabel("🟢 Aktif"))

        main_layout.addWidget(account_box)

        # ===================== PREFERENSI =====================
        pref_box = QGroupBox("Preferensi")
        pref_form = QFormLayout(pref_box)

        pref_form.addRow("Tema:", QLabel("Dark"))
        pref_form.addRow("Bahasa:", QLabel("Indonesia"))
        pref_form.addRow("Notifikasi:", QLabel("Aktif"))

        main_layout.addWidget(pref_box)

        # ===================== AKSI AKUN =====================
        action_box = QGroupBox("Aksi Akun")
        action_layout = QHBoxLayout(action_box)

        btn_edit = QPushButton("✏️ Edit Profil")
        btn_password = QPushButton("🔐 Ganti Password")
        btn_logout = QPushButton("🚪 Logout")

        btn_logout.setStyleSheet("color: #c0392b;")

        action_layout.addWidget(btn_edit)
        action_layout.addWidget(btn_password)
        action_layout.addStretch()
        action_layout.addWidget(btn_logout)

        main_layout.addWidget(action_box)
        main_layout.addStretch()
