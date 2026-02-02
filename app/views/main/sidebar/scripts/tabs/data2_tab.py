from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView, QMenu
from PySide6.QtCore import Qt
from shiboken6 import wrapInstance
from .detail.data2_window import Data2DetailWindow

class Data2Tab(QWidget):
    def __init__(self, proxy, selection_model, parent=None):
        super().__init__(parent)

        self.proxy = proxy

        layout = QVBoxLayout(self)
        self.table = QTableView(self)
        self.table.setModel(proxy)
        self.table.setSelectionModel(selection_model)

        self.table.setColumnHidden(0, True)
        self.table.setColumnHidden(1, True)
        self.table.setColumnHidden(2, True)
        self.table.setColumnHidden(3, True)
        self.table.setColumnHidden(4, True)
        self.table.setColumnHidden(5, True)
        self.table.setColumnHidden(6, True)
        self.table.setColumnHidden(7, True)
        self.table.setColumnHidden(8, True)
        self.table.setColumnHidden(9, True)
        self.table.setColumnHidden(10, True)
        self.table.setColumnHidden(11, True)
        self.table.setColumnHidden(12, True)
        self.table.setColumnHidden(13, True)
        self.table.setColumnHidden(14, True)
        self.table.setColumnHidden(15, True)
        self.table.setColumnHidden(16, True)
        self.table.setColumnHidden(17, True)
        self.table.setColumnHidden(18, True)
        self.table.setColumnHidden(19, True)
        self.table.setColumnHidden(20, True)
        self.table.setColumnHidden(21, True)
        self.table.setColumnHidden(22, True)
        self.table.setColumnHidden(23, True)
        self.table.setColumnHidden(24, True)
        self.table.setColumnHidden(25, True)
        self.table.setColumnHidden(26, True)
        self.table.setColumnHidden(27, True)
        self.table.setColumnHidden(28, True)
        self.table.setColumnHidden(29, True)
        self.table.setColumnHidden(30, True)
        self.table.setColumnHidden(31, True)
        self.table.setColumnHidden(32, True)

        # Double Click
        self.table.doubleClicked.connect(self.on_double_click)

        # Right Click
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(self.table)


        # Double Click
        self.table.doubleClicked.connect(self.on_double_click)

        # Right Click
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(self.table)


        # Double Click
        self.table.doubleClicked.connect(self.on_double_click)

        # Right Click
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(self.table)


        # Double Click
        self.table.doubleClicked.connect(self.on_double_click)

        # Right Click
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(self.table)


        # Double Click
        self.table.doubleClicked.connect(self.on_double_click)

        # Right Click
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(
                self.on_right_click
                )

        layout.addWidget(self.table)

    def on_double_click(self, index):
        if not index.isValid():
            return

        self.open_detail_window()

    def on_right_click(self, pos):
        index = self.table.indexAt(pos)
        if not index.isValid():
            return
        
        menu = QMenu(self)

        detail_action = menu.addAction("Detail")
        action = menu.exec(self.table.viewport().mapToGlobal(pos))

        if action == detail_action:
            self.open_detail_window()

    def open_detail_window(self):
        dialog = Data2DetailWindow(self)
        dialog.exec()


