from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
import datetime
from typing import Union

class ItemTableModel(QAbstractTableModel):
    """
    Model data untuk QTableView. Mengimplementasikan QAbstractTableModel 
    untuk menampilkan data daftar item (mis. skrip) dari API.
    
    Data diterima dalam format list of dicts:
    [{'id': 1, 'title': 'Skrip A', 'entry_date': '...', 'created_at': 1678886400}, ...]
    """
    
    # Kunci (keys) harus sesuai dengan respons JSON dari API
    DEFAULT_KEYS = ['id', 'title', 'entry_date', 'created_at'] 
    
    # Nama Header yang ditampilkan di UI, harus berurutan sesuai DEFAULT_KEYS
    DEFAULT_HEADERS = ["ID", "Judul Skrip", "Tgl. Masuk", "Dibuat Pada"]

    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._data = data if data is not None else []
        self._headers = self.DEFAULT_HEADERS
        self._keys = self.DEFAULT_KEYS

    def rowCount(self, parent=QModelIndex()):
        """Mengembalikan jumlah baris data."""
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        """Mengembalikan jumlah kolom."""
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        """Menyediakan data untuk ditampilkan di sel tabel berdasarkan Role."""
        if not index.isValid():
            return None
        
        row = index.row()
        col = index.column()

        # Batas keamanan
        if row >= len(self._data) or col >= len(self._keys):
            return None

        key = self._keys[col]
        value = self._data[row].get(key) # Menggunakan .get() untuk keamanan

        if role == Qt.DisplayRole:
            # 1. Konversi timestamp (hanya untuk kolom 'created_at')
            if key == 'created_at' and isinstance(value, (int, float)):
                try:
                    return datetime.datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')
                except ValueError:
                    return str(value) # Kembali ke nilai mentah jika konversi gagal
        
            # 2. Menampilkan None (Python/Null JSON) sebagai string kosong
            if value is None:
                return ""
                    
            # 3. Default: konversi ke string
            return str(value)
        
        if role == Qt.TextAlignmentRole:
            # Rata Kanan untuk ID (Kolom 0)
            if col == 0: 
                return int(Qt.AlignRight | Qt.AlignVCenter)
            # Rata Kiri untuk kolom lainnya
            return int(Qt.AlignLeft | Qt.AlignVCenter)
        
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Menyediakan nama header kolom atau nomor baris."""
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                # Header Kolom
                return self._headers[section] if 0 <= section < len(self._headers) else None
            
            if orientation == Qt.Vertical:
                # Nomor Baris
                return str(section + 1)
                
        return None 
    
    def update_data(self, data: list):
        """Memuat ulang model data dan memberi sinyal kepada View untuk refresh."""
        self.beginResetModel()
        self._data = data
        self.endResetModel()

    def get_item_at_row(self, row_index: int) -> Union[dict, None]:
        """Mengambil objek data asli (dict) dari baris tertentu."""
        if 0 <= row_index < len(self._data):
            return self._data[row_index]
        return None