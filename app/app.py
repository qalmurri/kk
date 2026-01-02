import sys
from PySide6.QtWidgets import QApplication
from views.auth.login_window import LoginWindow

def main():
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
