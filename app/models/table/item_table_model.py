from PySide6.QtCore import Qt, QAbstractTableModel

class DataTableModel(QAbstractTableModel):
    COLUMNS = [
        # Scripts
        {
            "id": "id",
            "key": "id",
            "label": "ID"
        },
        {
            "id": "title",
            "key": "title",
            "label": "Title"
        },
        {
            "id": "alias",
            "key": "alias",
            "label": "Alias"
        },
        {
            "id": "is_active",
            "key": "is_active",
            "label": "Active"
        },
        {
            "id": "entry_date",
            "key": "entry_date",
            "label": "Entry Date"
        },
        {
            "id": "finish_date",
            "key": "finish_date",
            "label": "Finish Date"
        },

        {
            "id": "institute",
            "key": "institute.name", 
            "label": "Institute"
        },
        {
            "id": "size",
            "key": "size.name",
            "label": "Size"
        },

        # Cover
        {
            "id": "process_desainer",
            "key": "process.bymade.user.username",
            "label": "Desainer",
            "where": {
                "process.sectionmade.name": "Desainer"
            }
        }, #sectionmade=desainer 
        {
            "id": "status_cover",
            "key": "status.sectionstatus.name",
            "label": "Status Cover",
            "where": {
                "status.labelstatus.name": "Desainer"
        }
        }, #labelstatus=desainer
        {
            "id": "cover.length",
            "key": "cover.length",
            "label": "Length"
        },
        {
            "id": "cover.height",
            "key": "cover.height",
            "label": "Height"
        },
        {
            "id": "cover.width",
            "key": "cover.width",
            "label": "Width"
        },
        {
            "id": "cover.x_axis",
            "key": "cover.x_axis",
            "label": "X_Axis"
        },
        {
            "id": "cover.y_axis",
            "key": "cover.y_axis",
            "label": "Y_Axis"
        },
        {
            "id": "cover.zoom",
            "key": "cover.zoom",
            "label": "Zoom"
        },
        {
            "id": "cover.thumbnail",
            "key": "cover.thumbnail",
            "label": "Thumbnail"
        },
        
        # Layouter
        {
            "id": "status_layouter",
            "key": "status.sectionstatus.name",
            "label": "Status Layouter"
        }, #labelstatus=layouter
        {
            "id": "pembuat_layouter",
            "key": "process.bymade.user.username",
            "label": "Pembuat"
        }, #sectionmade=layouter
        {
            "id": "flag_file",
            "key": "flag.is_active",
            "label": "File",
            "where": {
                "flag.sectionflag.name": "File"
                }
        }, #sectionflag=file
        {
            "id": "flag_photo",
            "key": "flag.is_active", 
            "label": "Photo",
            "where": {
                "flag.sectionflag.name": "Photo"
                }
        },#sectionflag=photo
        {
            "id": "flag_cv",
            "key": "flag.is_active",
            "label": "CV",
            "where": {
                "flag.sectionflag.name": "CV"
                }
        },#sectionflag=cv
        {
            "id": "flag_sinopsis",
            "key": "flag.is_active",
            "label": "Sinopsis",
            "where": {
                "flag.sectionflag.name": "Sinopsis"
                }
        },#sectionflag=sinopsis
        {
            "id": "flag_editor",
            "key": "flag.is_active",
            "label": "Editor",
            "where": {
                "flag.sectionflag.name": "Editor"
                }
        },#sectionflag=editor
        {
            "id": "flag_kata_pengantar",
            "key": "flag.is_active",
            "label": "Kata Pengantar",
            "where": {
                "flag.sectionflag.name": "Kata Pengantar"
                }
        },#sectionflag=kata_pengantar
        {
            "id": "flag_daftar_isi",
            "key": "flag.is_active",
            "label": "Daftar Isi",
            "where": {
                "flag.sectionflag.name": "Daftar Isi"
                }
        },#sectionflag=daftar_isi
        {
            "id": "flag_daftar_pustaka",
            "key": "flag.is_active",
            "label": "Daftar Pustaka",
            "where": {
                "flag.sectionflag.name": "Daftar Pustaka"
                }
        },#sectionflag=daftar_pustaka

        # Isbn
        {
            "key": "identification.isbn",
            "label": "ISBN"
        },
        {
            "key": "identification.typeisbn.name",
            "label": "Type"
        },
        
        # Produksi
        {
            "key": "status.sectionstatus.name",
            "label": "Produksi"
        }, #labelstatus=produksi
        {
            "key": "process.bymade.user.username",
            "label": "Pembuat"
        }, #sectionmade=produksi

        # orderers
        {
            "key": "orderers.orderer.name",
            "label": "Order"
        },
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
        column = self.COLUMNS[index.column()]
    
        key = column["key"]
        where = column.get("where")
    
        if where:
            return self.get_value_with_where(row, key, where)
    
        return self.get_value_by_path(row, key)

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

    @classmethod
    def column_index_by_key(cls, key: str) -> int:
        for i, col in enumerate(cls.COLUMNS):
            if col["key"] == key:
                return i
        return -1

    @classmethod
    def column_indexes_by_keys(cls, keys: set[str]) -> list[int]:
        return [
            i for i, col in enumerate(cls.COLUMNS)
            if col["key"] in keys
        ]

    @classmethod
    def column_indexes_by_ids(cls, ids: set[str]) -> list[int]:
        return [
            i for i, col in enumerate(cls.COLUMNS)
            if col.get("id") in ids
        ]

    def get_value_with_where(self, row, key, where: dict):
        root = key.split(".")[0]        # status
        items = row.get(root, [])
    
        if not isinstance(items, list):
            return None
    
        key_path = ".".join(key.split(".")[1:])  # sectionstatus.name
    
        for item in items:
            matched = True
    
            for where_key, expected in where.items():
                # where_key: status.labelstatus.name
                where_path = ".".join(where_key.split(".")[1:])  # labelstatus.name
                actual = self.get_value_by_path(item, where_path)
    
                if actual != expected:
                    matched = False
                    break
    
            if matched:
                return self.get_value_by_path(item, key_path)
    
        return None
