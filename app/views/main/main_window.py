from PySide6.QtWidgets import (
    QMainWindow, QTableView, QWidget, QVBoxLayout, QLabel
)
from controllers.main_controller import MainController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scripts")
        self.resize(1000, 600)

        self.table = QTableView()
        self.status_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.controller = MainController(self)
        self.table.doubleClicked.connect(self.on_row_double_click)

    def set_loading(self, loading: bool):
        self.status_label.setText("Loading data..." if loading else "")

    def show_error(self, message: str):
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.critical(self, "Error", message)

    def on_row_double_click(self, index):
        row = index.row()
        item = self.controller.model.get_item_at_row(row)
    
        if not item:
            return
    
        raw = item.get("_raw")
        if not raw:
            return
    
        from views.main.detail_dialog import DetailDialog
        dialog = DetailDialog(raw, self)
        dialog.exec()
