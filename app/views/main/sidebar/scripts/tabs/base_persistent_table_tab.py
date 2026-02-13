from PySide6.QtWidgets import QWidget, QTableView
from PySide6.QtCore import Qt
from core.session import Session
from models.table.item_table_model import DataTableModel

class BasePersistentTableTab(QWidget):
    TAB_KEY: str = None   # WAJIB di override

    def __init__(self, parent=None):
        super().__init__(parent)

        if not self.TAB_KEY:
            raise ValueError(
                f"{self.__class__.__name__} wajib mendefinisikan TAB_KEY"
            )

        self.table: QTableView | None = None

    # ===================== COLUMN PERSISTENCE =====================

    def enable_column_persistence(self):
        """Panggil SETELAH self.table dibuat"""
        header = self.table.horizontalHeader()

        header.sectionResized.connect(self._on_section_resized)
        self._restore_column_sizes()

    def _on_section_resized(self, logical_index: int, old_size: int, new_size: int):
        col = DataTableModel.COLUMNS[logical_index]
        col_id = col.get("id")

        if not col_id:
            return

        Session.set_table_column_width(
            self.TAB_KEY,
            col_id,
            new_size
        )

    def _restore_column_sizes(self):
        for logical_index, col in enumerate(DataTableModel.COLUMNS):
            col_id = col.get("id")
            if not col_id:
                continue

            size = Session.get_table_column_width(self.TAB_KEY, col_id)
            if size:
                self.table.setColumnWidth(logical_index, int(size))
