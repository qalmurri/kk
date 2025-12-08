from PySide6.QtCore import QObject, Signal, QSize, QModelIndex, QSettings
from core.api_client import APIClient
from core.auth_manager import AuthManager 
from views.ui_main_window import MainWindow
from models.item_model import ItemTableModel
from PySide6.QtWidgets import QMessageBox

class MainController(QObject):
    
    def __init__(self, api_client: APIClient, auth_manager: AuthManager):
        super().__init__()
        self.api_client = api_client
        self.auth_manager = auth_manager 
        self.settings = QSettings()
        print("MainController: Instance diinisialisasi.")
        
        self.model = ItemTableModel()
        self.view = MainWindow()
        self.view.table_view.setModel(self.model)

        self.load_column_widths()

        self.view.btn_refresh.clicked.connect(self.fetch_data)
        self.view.btn_add.clicked.connect(self.handle_add_item)
        self.view.btn_edit.clicked.connect(self.handle_edit_item)
        self.view.btn_delete.clicked.connect(self.handle_delete_item)
        
        self.view.action_refresh.triggered.connect(self.fetch_data)
        self.view.action_logout.triggered.connect(self.auth_manager.logout_user)
        self.view.action_exit.triggered.connect(self.view.close)

        self.view.action_add.triggered.connect(self.handle_add_item)
        self.view.action_edit.triggered.connect(self.handle_edit_item)
        self.view.action_delete.triggered.connect(self.handle_delete_item)

        self.view.table_view.doubleClicked.connect(self.handle_double_click)

        self.view.action_info_token.triggered.connect(self.show_token_info)
        self.view.action_info_user.triggered.connect(self.show_user_info)
        self.view.action_about.triggered.connect(self.show_about_info)

        self.view.table_view.customContextMenuRequested.connect(self._connect_context_menu_actions)
        
        self.view.table_view.horizontalHeader().setStretchLastSection(True)
        self.view.table_view.setMinimumSize(QSize(750, 550))


    def _connect_context_menu_actions(self, pos):
        """
        Menghubungkan aksi Context Menu ke controller saat menu dipanggil.
        """
        index = self.view.table_view.indexAt(pos)
        
        if index.isValid():
            try:
                self.view.action_table_edit.triggered.disconnect()
                self.view.action_table_delete.triggered.disconnect()
            except RuntimeError:
                pass

            self.view.action_table_edit.triggered.connect(self.handle_context_edit)
            self.view.action_table_delete.triggered.connect(self.handle_context_delete)
        
        self.view._show_context_menu(pos)


    def handle_context_edit(self):
        """Memanggil logika edit setelah aksi Context Menu diklik."""
        self.handle_edit_item()

    def handle_context_delete(self):
        """Memanggil logika delete setelah aksi Context Menu diklik."""
        self.handle_delete_item()

    def fetch_data(self):
        """Mengambil data item dari API dan memperbarui Model."""
        print("MainController: Memulai pengambilan data...")
        data = self.api_client.get_items()
        
        if data is not None:
            self.model.update_data(data)
            print(f"MainController: Data berhasil dimuat: {len(data)} baris.")
        else:
            QMessageBox.critical(self.view, "Error", "Gagal mengambil data dari server. Mungkin token kedaluwarsa.")
            print("MainController ERROR: Gagal mengambil data. Menampilkan pesan error.")

    def handle_add_item(self):
        print("MainController: Tombol Tambah ditekan. Buka form input...")
        pass

    def handle_edit_item(self): 
        selected_indexes = self.view.table_view.selectionModel().selectedRows()
        
        if not selected_indexes:
            QMessageBox.warning(self.view, "Peringatan", "Pilih baris yang ingin diedit.")
            print("MainController WARNING: Edit dibatalkan, tidak ada baris yang dipilih.")
            return

        row = selected_indexes[0].row()
        item_data = self.model.get_item_at_row(row)
        
        if item_data:
            print(f"MainController: Mengedit item ID: {item_data.get('id', 'N/A')} dan Judul: {item_data.get('title', 'N/A')}")

    def handle_delete_item(self):
        selected_indexes = self.view.table_view.selectionModel().selectedRows()
        if not selected_indexes:
            QMessageBox.warning(self.view, "Peringatan", "Pilih baris yang ingin dihapus.")
            print("MainController WARNING: Delete dibatalkan, tidak ada baris yang dipilih.")
            return

        row = selected_indexes[0].row()
        item_data = self.model.get_item_at_row(row)
        
        if item_data:
            reply = QMessageBox.question(self.view, 'Konfirmasi',
                f"Anda yakin ingin menghapus Item ID: {item_data['id']}?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                print(f"MainController: Menghapus item ID: {item_data['id']}...")
                print("MainController: Logic delete API akan dipanggil di sini.")
        pass

    def show_token_info(self):
        """Menampilkan token aktif saat ini."""
        token = self.api_client.get_token()
        
        if token:
            info = f"Token Aktif:\n\n{token[:10]}...{token[-5:]}"
            QMessageBox.information(self.view, "Info Token", info)
            print("MainController: Menampilkan Token Info.")
        else:
            QMessageBox.warning(self.view, "Info Token", "Tidak ada token aktif.")
            print("MainController WARNING: Menampilkan Info Token: Tidak ada token.")

    def show_user_info(self):
        """Menampilkan data user yang sedang login."""
        user_data = self.auth_manager.get_user_data()
        
        if self.auth_manager.is_authenticated():
            info = "Status: Login Berhasil\n"
            if user_data:
                info += f"Username: {user_data.get('username', 'N/A')}\n"
                info += f"ID: {user_data.get('id', 'N/A')}"
            else:
                info += "Data user belum dimuat. Hanya token yang tersedia."
                
            QMessageBox.information(self.view, "Info User Login", info)
            print("MainController: Menampilkan User Info.")
        else:
            QMessageBox.warning(self.view, "Info User Login", "Anda belum login.")
            print("MainController WARNING: Menampilkan User Info: Belum login.")

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
        print("MainController: Menampilkan About Info.")

    def handle_double_click(self, index: QModelIndex):
        """
        Menangani event double-click pada baris tabel.
        Menampilkan detail data baris tersebut dalam QMessageBox.
        """
        row = index.row() 
        item_data = self.model.get_item_at_row(row)

        if item_data:
            print(f"MainController: Double-click pada item ID: {item_data.get('id', 'N/A')}. Memuat detail...")
            detail_text = ""
            for key, value in item_data.items():
                if key == 'created_at':
                    import datetime
                    try:
                        value_str = datetime.datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')
                    except (TypeError, ValueError):
                        value_str = str(value)
                else:
                    value_str = str(value)

                detail_text += f"**{key.replace('_', ' ').title()}:** {value_str}\n"

            QMessageBox.information(
                self.view, 
                f"Detail Skrip ID: {item_data.get('id', 'N/A')}", 
                detail_text
            )
        else:
            QMessageBox.warning(self.view, "Error", "Gagal mengambil detail data baris ini.")
            print("MainController ERROR: Double-click gagal memuat detail data.")

    def save_column_widths(self):
        """Menyimpan lebar setiap kolom tabel ke QSettings."""
        
        table_view = self.view.table_view
        header = table_view.horizontalHeader()
        
        for i in range(header.count()):
            key = f"main_dashboard/column_width_{i}"
            self.settings.setValue(key, header.sectionSize(i))
        
        print("MainController: Pengaturan lebar kolom telah disimpan.")

    def load_column_widths(self):
        """Memuat lebar setiap kolom tabel dari QSettings dan menerapkannya."""
        
        table_view = self.view.table_view
        header = table_view.horizontalHeader()
        
        for i in range(header.count()):
            key = f"main_dashboard/column_width_{i}"
            
            width = self.settings.value(key, 150, type=int) 
            
            header.resizeSection(i, width)
        
        print("MainController: Load pengaturan lebar kolom.")