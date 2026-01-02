from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(300, 200)

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("IP Address Server")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Server IP"))
        layout.addWidget(self.ip_input)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_btn)

        from controllers.auth_controller import AuthController
        self.controller = AuthController(self)

    def show_error(self, message: str):
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.critical(self, "Error", message)

    def on_login_success(self):
        from views.main.main_window import MainWindow
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def set_loading(self, loading: bool):
        self.login_btn.setEnabled(not loading)
        self.login_btn.setText("Loading..." if loading else "Login")

