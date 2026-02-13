from PySide6.QtCore import Qt
from core.session import Session

class BaseTableTab:
    TAB_NAME = "base"  # override di child

    def setup_column_persistence(self):
        header = self.table.horizontalHeader()

        # save ketika user resize
        header.sectionResized.connect(self._on_section_resized)

        # restore setelah model siap
        self.restore_column_widths()

    def _on_section_resized(self, logicalIndex, oldSize, newSize):
        model = self.table.model().sourceModel()
        column = model.COLUMNS[logicalIndex]
        column_id = column.get("id") or column["key"]

        # GAK MUNCUL CUK!
        print(
            Session.get_table_column_width("cover", "id")
        )

        Session.set_table_column_width(
            self.TAB_NAME,
            column_id,
            newSize
        )

    def restore_column_widths(self):
        model = self.table.model().sourceModel()

        for i, column in enumerate(model.COLUMNS):
            column_id = column.get("id") or column["key"]
            width = Session.get_table_column_width(self.TAB_NAME, column_id)

            if width:
                self.table.setColumnWidth(i, width)
