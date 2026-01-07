from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex


class ItemTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # === NAMA KOLOM (PONDASI) ===
        self.headers = [
            "ID",
            "Name",
            "Category",
            "Status",
            "Created At",
            "Updated At"
        ]

        # === DATA KOSONG DULU ===
        self._data = []

    # ======================
    # REQUIRED METHODS
    # ======================
    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return ""  # kosong dulu

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.headers[section]

        return section + 1
