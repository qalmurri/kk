from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableView, QPushButton, QMenu, QAbstractItemView, QToolBar # <-- Tambahkan QAbstractItemView
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    """
    Jendela Utama Aplikasi yang menampilkan tabel data dengan Menu Bar dan Context Menu.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enterprise App - Main Dashboard")
        self.setGeometry(100, 100, 850, 650)
        
        # 1. SETUP MENU BAR
        self._setup_menu_bar()
        self._setup_toolbar()

        # Widget Utama (Central Widget)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # 2. Tabel Data
        self.table_view = QTableView()
        self.table_view.verticalHeader().hide()

        # --- PENGATURAN MODE SELEKSI BARU ---
        # 1. Memastikan seleksi selalu memilih seluruh baris
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 2. Memastikan hanya satu baris yang bisa dipilih (opsional, tapi disarankan untuk CRUD)
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_view.setMouseTracking(True) # Pastikan mouse tracking aktifWx

        # --- AKTIFKAN CONTEXT MENU ---
        self.table_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_view.customContextMenuRequested.connect(self._show_context_menu)
        # -----------------------------
        
        self.main_layout.addWidget(self.table_view)

        # 3. Kontrol CRUD (Tetap dipertahankan)
        self.crud_layout = QHBoxLayout()
        # ... (Kode tombol refresh, add, edit, delete sama seperti sebelumnya) ...
        self.btn_refresh = QPushButton("Refresh Data")
        self.btn_add = QPushButton("Tambah Baru (Create)")
        self.btn_edit = QPushButton("Edit (Update)")
        self.btn_delete = QPushButton("Hapus (Delete)")

        self.crud_layout.addWidget(self.btn_refresh)
        self.crud_layout.addStretch(1) 
        self.crud_layout.addWidget(self.btn_add)
        self.crud_layout.addWidget(self.btn_edit)
        self.crud_layout.addWidget(self.btn_delete)
        
        self.main_layout.addLayout(self.crud_layout)

# --- Metode untuk Setup Toolbar (BARU) ---
    def _setup_toolbar(self):
        """Membuat dan mengisi QToolBar dengan aksi dari Menu Bar."""
        
        # 1. Buat objek QToolBar
        self.toolbar = QToolBar("Main Operations")
        self.toolbar.setMovable(False) # Agar user tidak bisa memindahkan toolbar
        self.addToolBar(self.toolbar)

        # 2. Tambahkan aksi (action) ke Toolbar
        # Kita gunakan kembali QAction yang sudah didefinisikan di _setup_menu_bar
        
        # Aksi Utama Data (CRUD)
        self.toolbar.addAction(self.action_refresh)
        self.toolbar.addSeparator() # Pemisah visual
        self.toolbar.addAction(self.action_add)      # <-- Kita perlu aksi ini
        self.toolbar.addAction(self.action_edit)     # <-- Kita perlu aksi ini
        self.toolbar.addAction(self.action_delete)   # <-- Kita perlu aksi ini
        self.toolbar.addSeparator()

        # Aksi Logout
        self.toolbar.addAction(self.action_logout)
        
        # Catatan: Kita perlu memastikan QAction untuk Add, Edit, Delete juga didefinisikan
        # di _setup_menu_bar (atau di __init__) agar bisa diakses di sini.
        
        # Jika Anda tidak mendefinisikan action_add/edit/delete di Menu Bar,
        # Anda harus mendefinisikannya di sini dan menghubungkannya di Controller.

    def _setup_menu_bar(self):
        """Membuat struktur Menu Bar sederhana."""
        menu_bar = self.menuBar()
        self.menu_bar = menu_bar
        
        # Menu File
        self.menu_file = menu_bar.addMenu("&File")
        


# Definisikan Aksi CRUD sebagai atribut instance agar bisa diakses Toolbar
        self.action_add = QAction(QIcon.fromTheme("list-add"), "Tambah Baru", self)
        self.action_edit = QAction(QIcon.fromTheme("document-edit"), "Edit Data", self)
        self.action_delete = QAction(QIcon.fromTheme("list-remove"), "Hapus Data", self)
        
        # Aksi (Actions) File (seperti sebelumnya)
        self.action_refresh = QAction(QIcon.fromTheme("view-refresh"), "Refresh Data", self)
        self.action_logout = QAction(QIcon.fromTheme("system-log-out"), "Logout", self)
        self.action_exit = QAction(QIcon.fromTheme("application-exit"), "Exit", self)
        # Tambahkan Aksi ke Menu File
        self.menu_file.addAction(self.action_refresh)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_logout)
        self.menu_file.addAction(self.action_exit)

        # Menu Help (Opsional)
        self.menu_info = self.menu_bar.addMenu("&Info")
        self.action_info_token = QAction("Info Token Aktif", self)
        self.action_info_user = QAction("Info User Login", self)
        self.action_about = QAction("Tentang Aplikasi", self)       

        self.menu_info.addAction(self.action_info_token)
        self.menu_info.addAction(self.action_info_user)
        self.menu_info.addSeparator()
        self.menu_info.addAction(self.action_about)

    def _show_context_menu(self, pos):
        """Membuat dan menampilkan Context Menu saat klik kanan."""
        
        # Memastikan ada item yang dipilih
        index = self.table_view.indexAt(pos)
        if not index.isValid():
            return

        # 1. Buat Context Menu
        context_menu = QMenu(self)
        
        # 2. Buat Aksi CRUD untuk Context Menu
        self.action_table_edit = QAction("Edit Data...", self)
        self.action_table_delete = QAction("Hapus Data", self)
        
        # 3. Tambahkan Aksi ke Menu
        context_menu.addAction(self.action_table_edit)
        context_menu.addAction(self.action_table_delete)
        
        # 4. Tampilkan menu di posisi kursor
        context_menu.exec(self.table_view.viewport().mapToGlobal(pos))
        
        # Catatan: Koneksi sinyal (connect) dari action_table_edit/delete
        # ke fungsi kontrol akan dilakukan di MainController!