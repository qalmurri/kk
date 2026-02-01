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
        {"key": "status.sectionstatus", "label": "Status Cover"}, #labelstatus=desainer
        {"key": "process.bymade.user.username", "label": "Pembuat"}, #sectionmade=desainer 
        
        # Layouter
        {"key": "status.sectionstatus", "label": "Status Layouter"}, #labelstatus=layouter
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
        {"key": "identificaiton.typeisbn", "label": "Type"},
        
        # Produksi
        {"key": "status.sectionstatus", "label": "Produksi"}, #labelstatus=produksi
        {"key": "process.bymade.user.username", "label": "Pembuat"}, #sectionmade=produksi

        # orderers
        {"key": "orderers.orderer.name", "label": "Order"},
 
    ],
    HEADERS = [
        "id",
        "title",
        "alias",
        "is_active",
        "entry_date",
        "finish_date",
        "institute", 
        "size",

#DESAINER/COVER
        "Desainer" # <= Status (labelstatus & sectionstatus)
        "process", # <= process (bymade & sectionmade)
        "length",
        "height",
        "width",
        "x_axis",
        "y_axis",
        "zoom",

#LAYOTER
        "Layouter", # <= Status (labelstatus & sectionstatus)
        "process", # <= Process (bymade & sectionmade)
        "file", # flag <= (sectionflag & is_active)
        "photo", # flag <= (sectionflag & is_active)
        "cv", # flag <= (sectionflag & is_active)
        "sinopsis", # flag <= (sectionflag & is_active)
        "editor", # flag <= (sectionflag & is_active)
        "kata pengantar", # flag <= (sectionflag & is_active)
        "daftar isi", # flag <= (sectionflag & is_active)
        "daftar pustaka", # flag <= (sectionflag & is_active)

#ISBN
        "isbn", # <= status (labelstatus & sectionstatus)
        "identification", # <= (typeisbn & isbn)
        
#PRODUKSI
        "Produksi" # <= status (labelstatus & sectionstatus)
        "process", # <= process (bymade & sectionmade)
    ]

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
    
#     def columnCount(self, parent=None):
#         return len(self.COLUMNS)

#     def data(self, index, role=Qt.DisplayRole):
#         if not index.isValid() or role != Qt.DisplayRole:
#             return None
# 
#         row = self._data[index.row()]
#         column_def = self.COLUMNS[index.column()]
#         key = column_def["key"]
# 
#         return row.get[key]

#     def headerData(self, section, orientation, role):
#         if role == Qt.DisplayRole and orientation == Qt.Horizontal:
#             return self.COLUMNS[section]["label"]

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
        if column == 6:
            return row["x_axis"]
        
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.HEADERS[section]
