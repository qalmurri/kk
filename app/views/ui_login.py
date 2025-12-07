from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class LoginWidget(QWidget):
    """Widget UI untuk Login."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login Aplikasi Enterprise")
        self.layout = QVBoxLayout(self)
        
        self.label_status = QLabel("Masukkan kredensial Anda")
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Username")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton("Login")
        
        self.layout.addWidget(self.label_status)
        self.layout.addWidget(self.input_username)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.button_login)
        
        # UI tidak boleh mengandung logika API, ini harus di Controller
        # self.button_login.clicked.connect(...)