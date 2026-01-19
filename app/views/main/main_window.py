from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMenuBar,
    QMessageBox,
    QLabel,
    QListWidget,
    QStackedWidget,
)
from PySide6.QtCore import QSize, Qt
from core.session import Session
from network.ws_client import WebSocketClient
from controllers.auth.logout_controller import LogoutController
from .sub_menu import PreferencesDialog
from .sidebar import ScriptsPage

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # --- INITIALIZATION ---
        self.ws = WebSocketClient()
        self.ws.connected.connect(self.on_ws_connected)
        self.ws.disconnected.connect(self.on_ws_disconnected)
        self.ws.error.connect(self.on_ws_error)
        self.ws.connect()

        size = Session.load_main_window_size()
        self.resize(size if isinstance(size, QSize) else QSize(1000, 700))
        self.controller = LogoutController(self)

        # --- UI COMPONENTS ---
        self._setup_menu_bar()
        self._setup_sidebar()
        self._setup_main_content()
        self._setup_footer()

        # --- MAIN LAYOUT ---
        # Horizontal layout untuk Sidebar + Content Area
        self.body_layout = QHBoxLayout()
        self.body_layout.setContentsMargins(0, 0, 0, 0)
        self.body_layout.setSpacing(0)
        self.body_layout.addWidget(self.sidebar)
        self.body_layout.addWidget(self.main_stack)

        # Vertical layout utama
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setMenuBar(self.menu_bar)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addLayout(self.body_layout)
        self.main_layout.addLayout(self.footer_layout)

    def _setup_sidebar(self):
        """Membuat navigasi samping"""
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(160)
        self.sidebar.addItems(["Beranda", "Scripts", "Pear", "Chart"])
        self.sidebar.setCurrentRow(0)
        
        # Signal: Pindah halaman utama saat menu sidebar diklik
        self.sidebar.currentRowChanged.connect(self.on_sidebar_changed)

    def _setup_main_content(self):
        """Membuat kontainer halaman (Stacked Widget)"""
        self.main_stack = QStackedWidget()


        # --- HALAMAM 0: BERANDA
        self.pear_page = QWidget()
        pear_layout = QVBoxLayout(self.pear_page)
        pear_layout.addWidget(QLabel("Halaman Pear (kosong)"), alignment=Qt.AlignCenter)

        self.main_stack.addWidget(self.pear_page)

        # --- HALAMAN 1: Scripts  ---
        self.scripts_page = ScriptsPage(self)
        self.main_stack.addWidget(self.scripts_page)

        # --- HALAMAN 2: PEAR (KOSONGAN) ---
        self.pear_page = QWidget()
        pear_layout = QVBoxLayout(self.pear_page)
        pear_layout.addWidget(QLabel("Halaman Pear (kosong)"), alignment=Qt.AlignCenter)

        self.main_stack.addWidget(self.pear_page)
        
        # --- HALAMAN 3: Chart (KOSONGAN) ---
        self.chart_page = QWidget()
        chart_layout = QVBoxLayout(self.chart_page)
        chart_layout.addWidget(QLabel("Halaman chart (kosong)"), alignment=Qt.AlignCenter)

        self.main_stack.addWidget(self.chart_page)
        
    def _setup_menu_bar(self):
        self.menu_bar = QMenuBar(self)
        
        file_menu = self.menu_bar.addMenu("File")
        logout_action = file_menu.addAction("Logout")
        exit_action = file_menu.addAction("Exit")

        options_menu = self.menu_bar.addMenu("Options")
        preferences_action = options_menu.addAction("Preferences")

        help_menu = self.menu_bar.addMenu("Help")
        about_action = help_menu.addAction("About")

        logout_action.triggered.connect(self.controller.logout)
        exit_action.triggered.connect(self.close)
        preferences_action.triggered.connect(self.show_preferences)
        about_action.triggered.connect(self.show_about)

    def _setup_footer(self):
        self.status_label = QLabel("offline")
        self.status_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.status_label.setStyleSheet("color: gray; padding: 5px;")

        self.footer_layout = QHBoxLayout()
        self.footer_layout.addStretch()
        self.footer_layout.addWidget(self.status_label)

    def on_sidebar_changed(self, index):
        """Mengatur perpindahan StackedWidget berdasarkan klik sidebar"""
        self.main_stack.setCurrentIndex(index)

    # --- WS HANDLERS ---
    def on_ws_connected(self):
        self.status_label.setText("🟢 Online")
        self.status_label.setStyleSheet("color: green; padding: 5px;")

    def on_ws_disconnected(self):
        self.status_label.setText("🔴 Offline")
        self.status_label.setStyleSheet("color: red; padding: 5px;")

    def on_ws_error(self, message):
        # belum ada handler
        self.status_label.setText("⚠️ Error")
        self.status_label.setStyleSheet("color: orange; padding: 5px;")

    # --- EVENTS ---
    def closeEvent(self, event):
        if self.ws: self.ws.disconnect()
        Session.save_main_window_size(self.size())
        super().closeEvent(event)

    def show_about(self):
        QMessageBox.information(self, "About", "Gae dewe iki bro APP ne xixi")

    def show_preferences(self):
        dialog = PreferencesDialog(self)
        dialog.exec()
