from PySide6.QtWidgets import QApplication
from core.session import Session
from views.auth.login_window import LoginWindow
from views.main.main_window import MainWindow
import sys
# testing git

app = QApplication(sys.argv)

if Session.is_logged_in():
    window = MainWindow()
else:
    window = LoginWindow()

window.show()
sys.exit(app.exec())
