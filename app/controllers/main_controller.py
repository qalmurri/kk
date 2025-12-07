from PySide6.QtCore import QObject, Signal, QSize
from core.api_client import APIClient
from core.auth_manager import AuthManager 
from views.ui_main_window import MainWindow
from models.item_model import ItemTableModel
from PySide6.QtWidgets import QMessageBox

class MainController(QObject):
    # ... (kode lainnya) ...
    
    def __init__(self, api_client: APIClient, auth_manager: AuthManager):
        super().__init__()
        self.api_client = api_client
        self.auth_manager = auth_manager 
        
        self.model = ItemTableModel()
        self.view = MainWindow()
        self.view.table_view.setModel(self.model)

        # 1. KONEKSI SINYAL DARI TOMBOL (CRUD Bawah)
        self.view.btn_refresh.clicked.connect(self.fetch_data)
        self.view.btn_add.clicked.connect(self.handle_add_item)
        self.view.btn_edit.clicked.connect(self.handle_edit_item)
        self.view.btn_delete.clicked.connect(self.handle_delete_item)
        
        # 2. KONEKSI SINYAL DARI MENU BAR
        self.view.action_refresh.triggered.connect(self.fetch_data)
        self.view.action_logout.triggered.connect(self.auth_manager.logout_user)
        self.view.action_exit.triggered.connect(self.view.close) # Menutup jendela

# --- KONEKSI SINYAL INFO (BARU) ---
        self.view.action_info_token.triggered.connect(self.show_token_info)
        self.view.action_info_user.triggered.connect(self.show_user_info)
        self.view.action_about.triggered.connect(self.show_about_info)

        # 3. KONEKSI SINYAL DARI CONTEXT MENU
        # Kita menghubungkan sinyal saat Context Menu ditampilkan
        self.view.table_view.customContextMenuRequested.connect(self._connect_context_menu_actions)
        
        self.view.table_view.horizontalHeader().setStretchLastSection(True)
        self.view.table_view.setMinimumSize(QSize(750, 550))


    def _connect_context_menu_actions(self, pos):
        """
        Menghubungkan aksi Context Menu ke controller saat menu dipanggil.
        Ini memastikan bahwa aksi selalu mengambil data yang benar.
        """
        index = self.view.table_view.indexAt(pos)
        
        # Hanya menghubungkan jika item valid
        if index.isValid():
            # Hapus koneksi sebelumnya untuk menghindari koneksi berulang
            try:
                self.view.action_table_edit.triggered.disconnect()
                self.view.action_table_delete.triggered.disconnect()
            except RuntimeError:
                pass # Abaikan jika belum ada koneksi

            # Hubungkan aksi ke metode handler CRUD
            self.view.action_table_edit.triggered.connect(self.handle_context_edit)
            self.view.action_table_delete.triggered.connect(self.handle_context_delete)
        
        # Memanggil _show_context_menu untuk menampilkan menu
        self.view._show_context_menu(pos)


    # --- Metode Handler Khusus Context Menu ---
    
    def handle_context_edit(self):
        """Memanggil logika edit setelah aksi Context Menu diklik."""
        # Logika edit di sini harus memastikan baris yang dipilih masih valid
        self.handle_edit_item()

    def handle_context_delete(self):
        """Memanggil logika delete setelah aksi Context Menu diklik."""
        # Logika delete di sini harus memastikan baris yang dipilih masih valid
        self.handle_delete_item()

    def fetch_data(self):
        """Mengambil data item dari API dan memperbarui Model."""
        # APIClient harus sudah memiliki token saat ini dipanggil
        print("Mengambil data...")
        data = self.api_client.get_items()
        
        if data is not None:
            self.model.update_data(data)
            print(f"Data berhasil dimuat: {len(data)} baris.")
        else:
            QMessageBox.critical(self.view, "Error", "Gagal mengambil data dari server. Mungkin token kedaluwarsa.")
            # Di sini Anda bisa menambahkan sinyal untuk kembali ke halaman login

    # --- Metode untuk Operasi CRUD ---

    def handle_add_item(self):
        print("Tombol Tambah ditekan. Buka form input...")
        # Di sini akan ada logika menampilkan form dialog baru dan memanggil api_client.create_item()
        pass

    def handle_edit_item(self):
        # Ambil baris yang sedang dipilih
        selected_indexes = self.view.table_view.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(self.view, "Peringatan", "Pilih baris yang ingin diedit.")
            return

        row = selected_indexes[0].row()
        item_data = self.model.get_item_at_row(row)
        
        if item_data:
            print(f"Mengedit item ID: {item_data['id']}")
            # Di sini akan ada logika menampilkan form dialog dengan data yang sudah terisi
            # dan memanggil api_client.update_item(item_data['id'], new_data)
        pass

    def handle_delete_item(self):
        selected_indexes = self.view.table_view.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(self.view, "Peringatan", "Pilih baris yang ingin dihapus.")
            return

        row = selected_indexes[0].row()
        item_data = self.model.get_item_at_row(row)
        
        if item_data:
            reply = QMessageBox.question(self.view, 'Konfirmasi',
                f"Anda yakin ingin menghapus Item ID: {item_data['id']}?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                print(f"Menghapus item ID: {item_data['id']}...")
                # Di sini panggil: success = self.api_client.delete_item(item_data['id'])
                # if success: self.fetch_data() # Muat ulang data
        pass

    def show_token_info(self):
        """Menampilkan token aktif saat ini."""
        token = self.api_client._token # Akses langsung ke atribut _token di APIClient
        
        if token:
            info = f"Token Aktif:\n\n{token[:10]}...{token[-5:]}" # Menampilkan sebagian token
            QMessageBox.information(self.view, "Info Token", info)
        else:
            QMessageBox.warning(self.view, "Info Token", "Tidak ada token aktif.")

    def show_user_info(self):
        """Menampilkan data user yang sedang login."""
        user_data = self.auth_manager.get_user_data()
        
        if self.auth_manager.is_authenticated():
            info = "Status: Login Berhasil\n"
            if user_data:
                 # Jika server Django Anda mengembalikan data user, tampilkan di sini
                 info += f"Username: {user_data.get('username', 'N/A')}\n"
                 info += f"ID: {user_data.get('id', 'N/A')}"
            else:
                 # Jika server login hanya mengembalikan token, tampilkan ini
                 info += "Data user belum dimuat. Hanya token yang tersedia."
                 
            QMessageBox.information(self.view, "Info User Login", info)
        else:
            QMessageBox.warning(self.view, "Info User Login", "Anda belum login.")

    def show_about_info(self):
        """Menampilkan informasi tentang aplikasi."""
        about_text = (
            "Aplikasi Enterprise Desktop\n"
            "----------------------------\n"
            "Dibuat menggunakan Python & PySide6 (Qt).\n"
            "Arsitektur: MVC/MVP Skalabel.\n"
            "Backend API: Django Rest Framework."
        )
        QMessageBox.about(self.view, "Tentang Aplikasi", about_text)