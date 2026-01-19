from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QSplitter
from .widgets.cover_preview import CoverPreview
from PySide6.QtCore import QSortFilterProxyModel, Qt

class CoverTab(QWidget):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        splitter = QSplitter(Qt.Horizontal)
        
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(model)

        # 1. SETUP TABLE
        self.table = QTableView(self)
        self.table.setModel(self.proxy_model)

        self.table.setSortingEnabled(True)

        # --- TAMBAHKAN DUA BARIS INI UNTUK SELEKSI 1 BARIS ---
        # Memastikan yang terpilih adalah seluruh baris, bukan sel individu
        self.table.setSelectionBehavior(QTableView.SelectRows) 
        # Memastikan hanya bisa pilih satu baris dalam satu waktu
        self.table.setSelectionMode(QTableView.SingleSelection)
        # ---------------------------------------------------

        # setAlternatingRowColors untuk selang seling warna
        #self.table.setAlternatingRowColors(True)

        self.table.horizontalHeader().setStretchLastSection(True)
        
        # Sembunyikan kolom teknis jika diperlukan (contoh kolom 3 ke atas)
        # self.table.setColumnHidden(3, True) 
        
        # 2. SETUP PREVIEW
        self.preview = CoverPreview(self)
        
        splitter.addWidget(self.table)
        splitter.addWidget(self.preview)
        splitter.setSizes([400, 600]) # Atur proporsi awal
        layout.addWidget(splitter)

        # Connect signal
        self.table.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, selected, deselected):
        indexes = selected.indexes()
        if not indexes:
            return

        # 1. Ambil index dari tabel (Proxy Index)
        proxy_index = indexes[0]

        # 2. Petakan ke index model asli (Source Index)
        # Penting agar data tetap benar meski tabel sedang di-sort atau di-filter
        source_index = self.proxy_model.mapToSource(proxy_index)
        source_row = source_index.row()

        # 3. Ambil model asli (ScriptsTableModel) melalui proxy
        source_model = self.proxy_model.sourceModel()

        # 4. Ambil data dari list _data milik model asli
        data = source_model._data[source_row]

        # Kirim ke previewer
        self.preview.update_preview(data)
