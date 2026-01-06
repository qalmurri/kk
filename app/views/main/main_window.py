from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QMenuBar,
    QMenu,
    QMessageBox
)
from core.session import Session
from controllers.auth.logout_controller import LogoutController

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(500*300)

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
        about_action.triggered.connect(self.shot_about)

    def show_about(self):
        QMessageBox.information(
            self,
            "About",
            "Gae dewe iki bro APP ne xixi"
        )

    def logout(self):
        Session.clear_tokens()
        from views.auth.login_window import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()
