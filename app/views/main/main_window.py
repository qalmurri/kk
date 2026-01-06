from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMenuBar,
    QMenu,
    QMessageBox,
    QTabWidget,
    QLabel
)
from PySide6.QtCore import QSize
from core.session import Session
from network.ws_client import WebSocketClient
from controllers.auth.logout_controller import LogoutController
from views.preferences_dialog import PreferencesDialog

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

        # SIGNALS
        logout_action.triggered.connect(self.controller.logout)
        exit_action.triggered.connect(self.close)
        preferences_action.triggered.connect(self.show_preferences)
        about_action.triggered.connect(self.show_about)

        # TAB WIDGET (CONTENT)
        self.tabs = QTabWidget(self)

        self.tabs.addTab(self._build_dashboard_tab(), "Dashboard")
        self.tabs.addTab(self._build_data_tab(), "Data")
        self.tabs.addTab(self._build_activity_tab(), "Activity")

        # CONTENT
        layout = QVBoxLayout(self)
        layout.setMenuBar(self.menu_bar)
        layout.addWidget(self.tabs)

    def closeEvent(self, event):
        if self.ws:
            self.ws.disconnect()

        Session.save_main_window_size(self.size())
        
        return super().closeEvent(event)

    def on_ws_connected(self):
        print("WebSocket connected")

    def on_ws_disconnected(self):
        print("WebSocket disconnected")

    def on_ws_error(self, message):
        print("WS error:", message)

    def show_about(self):
        QMessageBox.information(
            self,
            "About",
            "Gae dewe iki bro APP ne xixi"
        )

    def show_preferences(self):
        dialog = PreferencesDialog(self)
        dialog.exec()

    def _build_dashboard_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Dashboard content here"))
        return widget

    def _build_data_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Data content here"))
        return widget

    def _build_activity_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(QLabel("Activity content here"))
        return widget