from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableView, 
    QPushButton, QMenu, QAbstractItemView, QToolBar, QMenuBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QPoint

class MainWindow(QMainWindow):
    """
    Jendela Utama Aplikasi. Menampilkan tabel data, Menu Bar, Toolbar, dan Context Menu.
    """
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle("Enterprise App - Main Dashboard")
        self.setGeometry(100, 100, 850, 650)
        
        # 1. Setup Aksi (Actions) - Harus dilakukan pertama
        self._setup_actions()
        
        # 2. Setup Menu Bar & Toolbar
        self._setup_menu_bar()
        self._setup_toolbar()

        # 3. Setup Central Widget (Tabel dan Tombol CRUD)
        self._setup_central_widget()
        
    def _setup_actions(self):
        """Mendefinisikan semua QAction yang akan digunakan di Menu, Toolbar, dan Context Menu."""
        
        # Aksi File/Sistem
        self.action_refresh = QAction(QIcon.fromTheme("view-refresh"), "Refresh Data", self)
        self.action_logout = QAction(QIcon.fromTheme("system-log-out"), "Logout", self)
        
        # Aksi CRUD (Data)
        self.action_add = QAction(QIcon.fromTheme("list-add"), "Tambah Baru...", self)
        self.action_edit = QAction(QIcon.fromTheme("document-edit"), "Edit Data...", self)
        self.action_delete = QAction(QIcon.fromTheme("list-remove"), "Hapus Data", self)
        
        # Aksi Info/Help
        self.action_info_token = QAction("Info Token Aktif", self)
        self.action_info_user = QAction("Info User Login", self)
        self.action_about = QAction("Tentang Aplikasi", self) 

    def _setup_menu_bar(self):
        """Membuat struktur Menu Bar sederhana."""
        menu_bar: QMenuBar = self.menuBar()
        
        # Menu File
        menu_file = menu_bar.addMenu("&File")
        menu_file.addAction(self.action_refresh)
        menu_file.addSeparator()
        menu_file.addAction(self.action_logout)

        # Menu Data (Opsional, untuk menampung CRUD Actions)
        menu_data = menu_bar.addMenu("&Data")
        menu_data.addAction(self.action_add)
        menu_data.addAction(self.action_edit)
        menu_data.addAction(self.action_delete)
        
        # Menu Info
        menu_info = menu_bar.addMenu("&Info")
        menu_info.addAction(self.action_info_token)
        menu_info.addAction(self.action_info_user)
        menu_info.addSeparator()
        menu_info.addAction(self.action_about)

    def _setup_toolbar(self):
        """Membuat dan mengisi QToolBar."""
        toolbar = QToolBar("Main Operations")
        toolbar.setMovable(False) 
        self.addToolBar(toolbar)

        # Tambahkan aksi utama ke Toolbar
        toolbar.addAction(self.action_refresh)
        toolbar.addSeparator()
        toolbar.addAction(self.action_add) 
        toolbar.addAction(self.action_edit) 
        toolbar.addAction(self.action_delete) 
        toolbar.addSeparator()
        toolbar.addAction(self.action_logout)
        
    def _setup_central_widget(self):
        """Mengatur Central Widget, QTableView, dan tombol CRUD."""
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QVBoxLayout(self.central_widget)

        # 1. Tabel Data (QTableView)
        self.table_view = QTableView()
        self.table_view.verticalHeader().hide()

        # Pengaturan Seleksi
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows) # Pilih seluruh baris
        self.table_view.setSelectionMode(QAbstractItemView.SingleSelection) # Hanya satu baris yang bisa dipilih
        self.table_view.setMouseTracking(True) 

        # Aktifkan Context Menu
        self.table_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_view.customContextMenuRequested.connect(self._show_context_menu)
        
        main_layout.addWidget(self.table_view)

        # 2. Kontrol CRUD (Bottom Layout)
        self.btn_refresh = QPushButton("Refresh Data")
        self.btn_add = QPushButton("Tambah Baru (Create)")
        self.btn_edit = QPushButton("Edit (Update)")
        self.btn_delete = QPushButton("Hapus (Delete)")

        self.crud_layout = QHBoxLayout()
        self.crud_layout.addWidget(self.btn_refresh)
        self.crud_layout.addStretch(1) 
        self.crud_layout.addWidget(self.btn_add)
        self.crud_layout.addWidget(self.btn_edit)
        self.crud_layout.addWidget(self.btn_delete)
        
        main_layout.addLayout(self.crud_layout)

    def _show_context_menu(self, pos: QPoint):
        """Membuat dan menampilkan Context Menu saat klik kanan di tabel."""
        
        # Pastikan ada item yang dipilih di bawah kursor
        if not self.table_view.indexAt(pos).isValid():
             return

        context_menu = QMenu(self)
        
        # Buat Aksi yang hanya digunakan di Context Menu
        # Menggunakan QAction baru agar bisa dihubungkan secara terpisah di Controller
        self.action_table_edit = QAction("Edit Data...", self)
        self.action_table_delete = QAction("Hapus Data", self)
        
        context_menu.addAction(self.action_table_edit)
        context_menu.addAction(self.action_table_delete)
        
        # Tampilkan menu di posisi kursor
        context_menu.exec(self.table_view.viewport().mapToGlobal(pos))