from PySide6.QtCore import Qt, QAbstractTableModel

class DataTableModel(QAbstractTableModel):
    COLUMNS = [
        # Scripts
        {"key": "id", "label": "ID"},
        {"key": "title", "label": "Title"},
        {"key": "alias", "label": "Alias"},
        {"key": "is_active", "label": "Active"},
        {"key": "entry_date", "label": "Entry Date"},
        {"key": "finish_date", "label": "Finish Date"},

        {"key": "institute.name", "label": "Institute"},
        {"key": "size.name", "label": "Size"},

        # Cover
        {"key": "cover.length", "label": "Length"},
        {"key": "cover.height", "label": "Height"},
        {"key": "cover.width", "label": "Width"},
        {"key": "cover.x_axis", "label": "X_Axis"},
        {"key": "cover.y_axis", "label": "Y_Axis"},
        {"key": "cover.zoom", "label": "Zoom"},
        {"key": "cover.thumbnail", "label": "Thumbnail"},
        {"key": "status.sectionstatus.name", "label": "Status Cover"}, #labelstatus=desainer
        {"key": "process.bymade.user.username", "label": "Pembuat"}, #sectionmade=desainer 
        
        # Layouter
        {"key": "status.sectionstatus.name", "label": "Status Layouter"}, #labelstatus=layouter
        {"key": "process.bymade.user.username", "label": "Pembuat"}, #sectionmade=layouter
        {"key": "flag.is_active", "label": "File"}, #sectionflag=file
        {"key": "flag.is_active", "label": "Photo"},#sectionflag=photo
        {"key": "flag.is_active", "label": "CV"},#sectionflag=cv
        {"key": "flag.is_active", "label": "Sinopsis"},#sectionflag=sinopsis
        {"key": "flag.is_active", "label": "Editor"},#sectionflag=editor
        {"key": "flag.is_active", "label": "Kata Pengantar"},#sectionflag=kata_pengantar
        {"key": "flag.is_active", "label": "Daftar Isi"},#sectionflag=daftar_isi
        {"key": "flag.is_active", "label": "Daftar Pustaka"},#sectionflag=daftar_pustaka

        # Isbn
        {"key": "identification.isbn", "label": "ISBN"},
        {"key": "identification.typeisbn.name", "label": "Type"},
        
        # Produksi
        {"key": "status.sectionstatus.name", "label": "Produksi"}, #labelstatus=produksi
        {"key": "process.bymade.user.username", "label": "Pembuat"}, #sectionmade=produksi

        # orderers
        {"key": "orderers.orderer.name", "label": "Order"},
 
    ]

    def __init__(self, parent=None):
         super().__init__(parent)
         self._data = []
#             {
#                 "id": 1,
#                 "thumbnail": "cover2.jpeg",
#                 "length": 12,
#                 "height": 210,
#                 "width": 148,
#                 "x_axis": -2,
#                 "y_axis": 0,
#                 "zoom": 0.195 ,
# 
#                 "title": "Cover A", #script_id
#                 "status": "Draft"
#             },
#             {
#                 "id": 2,
#                 "thumbnail": "cover.jpeg",
#                 "length": 15,
#                 "height": 100,
#                 "width": 50,
#                 "x_axis": 0,
#                 "y_axis": 0,
#                 "zoom": 0.3,
# 
#                 "title": "Cover B", #script_id
#                 "status": "Published",
#             },
#             {
#                 "id": 3,
#                 "thumbnail": "None",
#                 "length": 20,
#                 "height": 50,
#                 "width": 25,
#                 "x_axis": 0,
#                 "y_axis": 0,
#                 "zoom": 0.2,
# 
#                 "title": "Cover C",
#                 "status": "Published",
#             },
#             {
#                 "id": 4,
#                 "thumbnail": "None",
#                 "length": 25,
#                 "height": 330,
#                 "width": 215,
#                 "x_axis": 0,
#                 "y_axis": 0,
#                 "zoom": 0.2,
# 
#                 "title": "Cover C", #script_id
#                 "status": "Published",
#             },
#             {
#                 "id": 5,
#                 "thumbnail": "None",
#                 "length": 25,
#                 "height": 210,
#                 "width": 148,
#                 "x_axis": 0,
#                 "y_axis": 0,
#                 "zoom": 0.2,
# 
#                 "title": "Cover C", #script_id
#                 "status": "Published",
#             }
#         ]

    def rowCount(self, parent=None):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
         if not index.isValid() or role != Qt.DisplayRole:
             return None
 
         row = self._data[index.row()]
         column_def = self.COLUMNS[index.column()]
         key = column_def["key"]
 
         value = self.get_value_by_path(row, key)
         return value

    # MULAI REPATCH
    def get_value_by_path(self, data, path):
        parts = path.split(".")
        current = data
    
        for i, part in enumerate(parts):
            if current is None:
                return None
    
            if isinstance(current, list):
                values = []
                for item in current:
                    v = self.get_value_by_path(item, ".".join(parts[i:]))
                    if v not in (None, "", []):
                        values.append(str(v))
                return ", ".join(values) if values else None
    
            if isinstance(current, dict):
                current = current.get(part)
            else:
                return None
    
        return current

    def columnCount(self, parent=None):
        return len(self.COLUMNS)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.COLUMNS[section]["label"]

    def set_api_data(self, api_data):
        if not isinstance(api_data, list):
            print("set_api_data expects list, got:", type(api_data))
            return

        self.beginResetModel()
        rows = []

        for script in api_data:
            covers = script.get("cover", [])

            # kalau tidak ada cover => 1 row
            if not covers:
                row = script.copy()
                row["cover"] = {}
                rows.append(row)
                continue

            # 1 cover = 1 row
            for cover in covers:
                row = script.copy()
                row["cover"] = cover
                rows.append(row)

        self._data = rows
        self.endResetModel()



