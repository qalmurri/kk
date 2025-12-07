from PySide6.QtWidgets import QDialog, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class LoginDialog(QDialog):
    """Jendela Login Modal Mandiri (Small Window)."""
    def __init__(self, login_widget: QWidget, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login Aplikasi Enterprise")
        
        # 1. Atur ukuran tetap kecil
        self.setFixedSize(400, 300) 
        
        # 2. Sisipkan LoginWidget (UI)
        self.login_widget = login_widget 
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.login_widget)

        # 3. Atur sebagai modal
        self.setModal(True)
        
        # Opsional: Hapus tombol maximize/minimize
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint & ~Qt.WindowMinimizeButtonHint)
        
        # Opsional: Anda dapat menghubungkan tombol Login di sini untuk memanggil self.accept()
        # self.login_widget.button_login.clicked.connect(self.accept) 
        # TAPI KONEKSI LEBIH BAIK DI CONTROLLER