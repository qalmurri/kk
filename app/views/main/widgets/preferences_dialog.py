from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QWidget,
    QCheckBox,
    QPushButton,
    QLabel
)

class PreferencesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preferences")
        self.setModal(True)
        self.resize(400, 250)

        layout = QVBoxLayout(self)

        # ===== TABS =====
        tabs = QTabWidget()

        # --- General Tab ---
        general_tab = QWidget()
        general_layout = QVBoxLayout(general_tab)

        self.start_minimized_cb = QCheckBox("Start minimized")
        self.notifications_cb = QCheckBox("Enable notifications")

        general_layout.addWidget(self.start_minimized_cb)
        general_layout.addWidget(self.notifications_cb)
        general_layout.addStretch()

        tabs.addTab(general_tab, "General")

        # --- Advanced Tab ---
        advanced_tab = QWidget()
        advanced_layout = QVBoxLayout(advanced_tab)

        self.debug_cb = QCheckBox("Enable debug mode")
        advanced_layout.addWidget(self.debug_cb)
        advanced_layout.addStretch()

        tabs.addTab(advanced_tab, "Advanced")

        layout.addWidget(tabs)

        # ===== BUTTONS =====
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        cancel_btn = QPushButton("Cancel")
        ok_btn = QPushButton("OK")

        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(ok_btn)

        layout.addLayout(btn_layout)

        # ===== SIGNALS =====
        cancel_btn.clicked.connect(self.reject)
        ok_btn.clicked.connect(self.accept)