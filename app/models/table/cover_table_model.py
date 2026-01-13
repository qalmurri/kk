from PySide6.QtCore import Qt, QAbstractTableModel

class CoverTableModel(QAbstractTableModel):
    HEADERS = ["ID", "Title", "Status"]

    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = [
            {
                "id": 1,
                "title": "Cover A",
                "status": "Draft",
                "thumbnail": "https://",
                "length": 10,
                "height": 250,
                "width": 160,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0
            },
            {
                "id": 2,
                "title": "Cover B",
                "status": "Published",
                "thumbnail": "cover.jpeg",
                "length": 10,
                "height": 250,
                "width": 160,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0
            },
        ]

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self.HEADERS)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None

        row = self._data[index.row()]
        column = index.column()

        if column == 0:
            return row["id"]
        if column == 1:
            return row["title"]
        if column == 2:
            return row["status"]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.HEADERS[section]
