# views/auth/login_window.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
)
from core.session import Session

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(300, 200)

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Server IP")
        self.ip_input.setText(Session.get_backend_ip())

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")

        layout = QVBoxLayout(self)
        layout.addWidget(self.ip_input)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_btn)

        from controllers.auth.login_controller import LoginController
        self.controller = LoginController(self)

    def set_loading(self, loading: bool):
        self.login_btn.setEnabled(not loading)
        self.login_btn.setText("Loading..." if loading else "Login")

    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)

    def on_login_success(self):
        from views.main.main_window import MainWindow
        self.main = MainWindow()   # WAJIB disimpan
        self.main.show()
        self.close()
