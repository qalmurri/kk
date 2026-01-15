from PySide6.QtCore import Qt, QAbstractTableModel

class CoverTableModel(QAbstractTableModel):
    HEADERS = ["ID", "Title", "Status"]

    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = [
            {
                "id": 1,
                "created_at": "",
                "updated_at": "",
                "thumbnail": "cover2.jpeg",
                "length": 12,
                "height": 210,
                "width": 148,
                "x_axis": -2,
                "y_axis": 0,
                "zoom": 0.195 ,

                "title": "Cover A", #script_id
                "status": "Draft"
            },
            {
                "id": 2,
                "created_at": "",
                "updated_at": "",
                "thumbnail": "cover.jpeg",
                "length": 15,
                "height": 250,
                "width": 160,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0.3,

                "title": "Cover B", #script_id
                "status": "Published",
            },
            {
                "id": 3,
                "created_at": "",
                "updated_at": "",
                "thumbnail": "None",
                "length": 20,
                "height": 250,
                "width": 160,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0.2,

                "title": "Cover C",
                "status": "Published",
            },
            {
                "id": 4,
                "created_at": "",
                "updated_at": "",
                "thumbnail": "None",
                "length": 25,
                "height": 250,
                "width": 160,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0.2,

                "title": "Cover C", #script_id
                "status": "Published",
            },
            {
                "id": 5,
                "created_at": "",
                "updated_at": "",
                "thumbnail": "None",
                "length": 25,
                "height": 250,
                "width": 160,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0.2,

                "title": "Cover C", #script_id
                "status": "Published",
            }
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
