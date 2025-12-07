from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
# QVariant SUDAH DIHAPUS karena tidak diperlukan di PySide6 modern

class ItemTableModel(QAbstractTableModel):
    """
    Model data untuk QTableView yang mengambil data dari server backend.
    """
    
    def __init__(self, data=None, headers=None, parent=None):
            super().__init__(parent)
            self._data = data if data is not None else []

            # --- PERUBAHAN PENTING PADA HEADER DAN KEYS ---
            self._headers = headers if headers is not None else ["ID", "Judul Skrip", "Tgl. Masuk", "Dibuat Pada"]
            # Kunci harus sesuai dengan JSON API baru
            self._keys = ['id', 'title', 'entry_date', 'created_at'] 
            # ---------------------------------------------

    def rowCount(self, parent=QModelIndex()):
        """Mengembalikan jumlah baris."""
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        """Mengembalikan jumlah kolom."""
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
            """Menyediakan data untuk ditampilkan di sel."""
            if not index.isValid():
                return None
            
            row = index.row()
            col = index.column()
    
            if role == Qt.DisplayRole:
                key = self._keys[col]
                value = self._data[row].get(key, '')
    
                # Konversi timestamp 'created_at' menjadi format tanggal/waktu yang mudah dibaca (opsional)
                if key == 'created_at' and isinstance(value, (int, float)):
                    import datetime
                    return datetime.datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')
    
                # Menampilkan 'null' sebagai string kosong untuk entry_date
                if value is None:
                    return ""
                    
                return str(value)
            
            # Contoh tambahan role untuk perataan teks
            if role == Qt.TextAlignmentRole:
                if col == 0: # Hanya ID yang rata kanan
                    return int(Qt.AlignRight | Qt.AlignVCenter)
                return int(Qt.AlignLeft | Qt.AlignVCenter)
            
            return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Menyediakan nama header kolom/baris."""
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
            # Jika orientasi Vertical (nomor baris)
            if orientation == Qt.Vertical:
                return str(section + 1)
        return None # <-- Ganti QVariant() menjadi None
    
    def update_data(self, data):
        """Memuat ulang data tabel setelah pengambilan API atau CRUD."""
        self.beginResetModel()
        self._data = data
        self.endResetModel()

    def get_item_at_row(self, row_index):
        """Mengambil objek data asli (dict) dari baris tertentu."""
        if 0 <= row_index < len(self._data):
            return self._data[row_index]
        return None