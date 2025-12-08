from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import QSettings

class LoginWidget(QWidget):
    """Widget UI yang berisi form input URL, Username, dan Password."""
    def __init__(self):
        super().__init__()
        
        settings = QSettings()
        
        # 1. Input URL (Diisi dari QSettings jika ada, atau default)
        saved_url = settings.value("app/base_url", "http://127.0.0.1:8000/", type=str)
        self.input_url = QLineEdit(saved_url) 
        self.input_url.setPlaceholderText("Alamat Server API (e.g., http://localhost:8000/)")

        # 2. Input Username & Password
        self.input_username = QLineEdit()
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        # 3. Button & Status
        self.button_login = QPushButton("Login")
        self.label_status = QLabel("")
        
        # 4. Layout
        layout = QVBoxLayout(self)
        
        # Tambahkan URL ke layout
        layout.addWidget(QLabel("Server URL:"))
        layout.addWidget(self.input_url)
        
        # Tambahkan Username & Password
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.input_username)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.input_password)
        
        # Tambahkan Tombol dan Status
        layout.addSpacing(15)
        layout.addWidget(self.button_login)
        layout.addWidget(self.label_status)
        layout.addStretch(1)