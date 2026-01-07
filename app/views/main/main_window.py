from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMenuBar,
    QMenu,
    QMessageBox,
    QTabWidget,
    QLabel,
)
from PySide6.QtCore import QSize, Qt
from core.session import Session
from network.ws_client import WebSocketClient
from controllers.auth.logout_controller import LogoutController
from views.preferences_dialog import PreferencesDialog

from views.tabs import DataTab, ActivityTab, DashboardTab, CoverTab

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # WEBSOCKET
        self.ws = WebSocketClient()
        self.ws.connected.connect(self.on_ws_connected)
        self.ws.disconnected.connect(self.on_ws_disconnected)
        self.ws.error.connect(self.on_ws_error)
        self.ws.connect()

        # PENYIMPANAN SIZE WINDOW
        size = Session.load_main_window_size()
        if isinstance(size, QSize):
            self.resize(size)
        else:
            self.resize(500, 500)

        # CONTROLLER
        self.controller = LogoutController(self)

        # MASTER & MENU FILE
        self.menu_bar = QMenuBar(self)
        file_menu = QMenu("File", self)
        self.menu_bar.addMenu(file_menu)
        logout_action = file_menu.addAction("Logout")
        exit_action = file_menu.addAction("Exit")

        # MENU OPTION
        options_menu = QMenu("Options", self)
        self.menu_bar.addMenu(options_menu)
        preferences_action = options_menu.addAction("Preferences")

        # MENU HELP
        help_menu = QMenu("Help", self)
        self.menu_bar.addMenu(help_menu)
        about_action = help_menu.addAction("About")

        # FOOTER
        self.status_label = QLabel("offline")
        self.status_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.status_label.setStyleSheet("color: gray;")

        footer_layout = QHBoxLayout()
        footer_layout.addStretch()
        footer_layout.addWidget(self.status_label)

        # SIGNALS
        logout_action.triggered.connect(self.controller.logout)
        exit_action.triggered.connect(self.close)
        preferences_action.triggered.connect(self.show_preferences)
        about_action.triggered.connect(self.show_about)

        # TAB WIDGET (CONTENT)
        self.tabs = QTabWidget(self)
        self.tabs.addTab(DashboardTab(self), "Dashboard")
        self.tabs.addTab(DataTab(self), "Data")
        self.tabs.addTab(ActivityTab(self), "Activity")
        self.tabs.addTab(CoverTab(self), "Cover")

        # CONTENT
        layout = QVBoxLayout(self)
        layout.setMenuBar(self.menu_bar)
        layout.addWidget(self.tabs)
        layout.addLayout(footer_layout)

    def closeEvent(self, event):
        if self.ws:
            self.ws.disconnect()

        Session.save_main_window_size(self.size())
        return super().closeEvent(event)

    def on_ws_connected(self):
        self.status_label.setText("🟢 Online")
        self.status_label.setStyleSheet("color: green;")

    def on_ws_disconnected(self):
        self.status_label.setText("🔴 Offline")
        self.status_label.setStyleSheet("color: red;")

    def on_ws_error(self, message):
        self.status_label.setText("⚠️ Error")
        self.status_label.setStyleSheet("color: orange;")

    def show_about(self):
        QMessageBox.information(
            self,
            "About",
            "Gae dewe iki bro APP ne xixi"
        )

    def show_preferences(self):
        dialog = PreferencesDialog(self)
        dialog.exec()