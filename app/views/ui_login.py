from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import QSettings

class LoginWidget(QWidget):
    """Widget UI yang berisi form input URL, Username, dan Password untuk proses Login."""
    
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self._setup_ui()
        
    def _setup_ui(self):
        """Membuat dan mengatur semua elemen UI dan layout."""
        
        settings = QSettings()
        
        # --- Input Fields ---
        
        # 1. Input URL (Menggunakan nilai dari QSettings atau default)
        saved_url = settings.value("app/base_url", "http://127.0.0.1:8000/", type=str)
        self.input_url = QLineEdit(saved_url) 
        self.input_url.setPlaceholderText("Alamat Server API (e.g., http://localhost:8000/)")

        # 2. Input Username & Password
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Masukkan Username Anda")
        
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Masukkan Password Anda")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        # --- Button & Status ---
        
        self.button_login = QPushButton("Login")
        self.label_status = QLabel("") # Digunakan untuk menampilkan pesan error/status
        
        # --- Layout ---
        
        layout = QVBoxLayout(self)
        
        # URL
        layout.addWidget(QLabel("Server URL:"))
        layout.addWidget(self.input_url)
        
        # Username
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.input_username)
        
        # Password
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.input_password)
        
        # Tombol dan Status
        layout.addSpacing(15)
        layout.addWidget(self.button_login)
        layout.addWidget(self.label_status)
        layout.addStretch(1) # Memastikan elemen berada di atas