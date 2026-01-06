from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMenuBar,
    QMenu,
    QMessageBox
)
from PySide6.QtCore import QSize
from core.session import Session
from controllers.auth.logout_controller import LogoutController

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # PENYIMPANAN SIZE WINDOW
        size = Session.load_main_window_size()
        if isinstance(size, QSize):
            self.resize(size)
        else:
            self.resize(500, 500)

        # MENU  BAR
        self.menu_bar = QMenuBar(self)

        # FILE MENU
        file_menu = QMenu("File", self)
        self.menu_bar.addMenu(file_menu)

        logout_action = file_menu.addAction("Logout")
        exit_action = file_menu.addAction("Exit")

        # HELP MENU
        help_menu = QMenu("Help", self)
        self.menu_bar.addMenu(help_menu)

        about_action = help_menu.addAction("About")

        # CONTENT
        self.logout_btn = QPushButton("Logout")

        layout = QVBoxLayout(self)
        layout.setMenuBar(self.menu_bar)
        layout.addStretch()
        layout.addWidget(self.logout_btn)
        layout.addStretch()

        # CONTROLLER
        self.controller = LogoutController(self)

        # SIGNALS
        self.logout_btn.clicked.connect(self.controller.logout)
        logout_action.triggered.connect(self.controller.logout)
        exit_action.triggered.connect(self.close)
        about_action.triggered.connect(self.show_about)

    def show_about(self):
        QMessageBox.information(
            self,
            "About",
            "Gae dewe iki bro APP ne xixi"
        )

    def closeEvent(self, event):
        Session.save_main_window_size(self.size())
        return super().closeEvent(event)

    def logout(self):
        Session.clear_tokens()
        from views.auth.login_window import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()
