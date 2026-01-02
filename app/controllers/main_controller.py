from utils.workers import LoadScriptsWorker
from utils.formatter import flatten_scripts
from models.table.item_table_model import ItemTableModel

class MainController:
    def __init__(self, view):
        self.view = view
        self.worker = None

        self.model = ItemTableModel()
        self.view.table.setModel(self.model)

        self.load_data()

    def load_data(self):
        self.view.set_loading(True)

        self.worker = LoadScriptsWorker()
        self.worker.success.connect(self.on_success)
        self.worker.error.connect(self.on_error)
        self.worker.start()

    def on_success(self, data: list):
        flat = flatten_scripts(data)
        self.model.update_data(flat)
        self.view.set_loading(False)

    def on_error(self, message: str):
        self.view.set_loading(False)
        self.view.show_error(message)
