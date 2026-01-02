from PySide6.QtWidgets import QDialog, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class LoginDialog(QDialog):
    """Jendela Login Modal Mandiri. 
    Menggunakan QDialog sebagai wadah untuk LoginWidget.
    """
    def __init__(self, login_widget: QWidget, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Login KK")
        
        # 1. Atur ukuran tetap kecil
        self.setFixedSize(200, 250) 
        
        # 2. Setup Layout dan Sisipkan LoginWidget
        self.login_widget = login_widget 
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.login_widget)

        # 3. Atur sebagai modal (Blokir input ke jendela lain)
        self.setModal(True)
        
        # 4. Hapus tombol maximize/minimize untuk tampilan login yang ringkas
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint & ~Qt.WindowMinimizeButtonHint)
        
        # Catatan: Logika koneksi tombol Login ke accept() atau controller 
        # dilakukan di LoginController, bukan di View ini.