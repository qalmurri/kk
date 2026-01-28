from PySide6.QtCore import Qt, QAbstractTableModel

class DataTableModel(QAbstractTableModel):
#      def set_data(self, data):
#         self.beginResetModel()
#         self._data = data
#         self.endResetModel()
        
    HEADERS = [
        "id",
        "title",
        "alias",
        "is_active",
        "entry_date",
        "finish_date",

#         #one-to-one
#         "institute", 
#         "size",
# 
#         #one-to-many
#         "orderers",
#         "status",
#         "flag",
#         "identification",
#         "process",
#         "cover",


# 
#         "Status",
#         "length",
#         "height",
#         "width",
#         "x_axis",
#         "y_axis",
#         "zoom"
    ]

    def transform_api_data(self, scripts: list[dict]) -> list[dict]:
        rows = []

        for script in scripts:
            covers = script.get("cover", [])

            # Kalau tidak ada cover → tetap buat 1 row
            if not covers:
                rows.append(self._base_row(script, cover=None))
                continue

            # Kalau ada cover → 1 cover = 1 row
            for cover in covers:
                rows.append(self._base_row(script, cover))

        return rows

    def _base_row(self, script: dict, cover: dict | None):
        institute = script.get("institute") or {}
        size = script.get("size") or {}

        return {
            "id": script.get("id"),
            "title": script.get("title"),
            "alias": script.get("alias"),
            "is_active": script.get("is_active"),

            # one-to-one (diringkas)
            "institute": institute.get("name"),
            "size": size.get("name"),

            # status ringkas (Layouter: Belum | ISBN: Sudah)
            "status": self._format_status(script.get("status", [])),

            # cover
            "thumbnail": cover.get("thumbnail") if cover else None,
            "length": cover.get("length") if cover else None,
            "height": cover.get("height") if cover else None,
            "width": cover.get("width") if cover else None,
            "x_axis": cover.get("x_axis") if cover else 0,
            "y_axis": cover.get("y_axis") if cover else 0,
            "zoom": self._calc_zoom(size, cover),
        }

    def _format_status(self, statuses: list[dict]) -> str:
        result = []

        for s in statuses:
            label = s.get("labelstatus", {}).get("name")
            section = s.get("sectionstatus", {}).get("name")

            if label and section:
                result.append(f"{label}: {section}")

        return " | ".join(result)

    def _calc_zoom(self, size: dict, cover: dict | None):
        if not cover:
            return 0.2
    
        try:
            return round(160 / cover["width"], 3)
        except Exception:
            return 0.2

    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = [
            {
                "id": 1,
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
                "thumbnail": "cover.jpeg",
                "length": 15,
                "height": 100,
                "width": 50,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0.3,

                "title": "Cover B", #script_id
                "status": "Published",
            },
            {
                "id": 3,
                "thumbnail": "None",
                "length": 20,
                "height": 50,
                "width": 25,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0.2,

                "title": "Cover C",
                "status": "Published",
            },
            {
                "id": 4,
                "thumbnail": "None",
                "length": 25,
                "height": 330,
                "width": 215,
                "x_axis": 0,
                "y_axis": 0,
                "zoom": 0.2,

                "title": "Cover C", #script_id
                "status": "Published",
            },
            {
                "id": 5,
                "thumbnail": "None",
                "length": 25,
                "height": 210,
                "width": 148,
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
            return row["alias"]
        if column == 3:
            return row["is_active"]
        if column == 4:
            return row["entry_date"]
        if column == 5:
            return row["finish_date"]
        
#         if column == 6:
#             return row["institute"]
#         if column == 7:
#             return row["size"]
#         
#         if column == 8:
#             return row["orderers"]
#         if column == 9:
#             return row["status"]
#         if column == 10:
#             return row["flag"]
#         if column == 11:
#             return row["identification"]
#         if column == 12:
#             return row["process"]
#         if column == 13:
#             return row["cover"]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.HEADERS[section]
