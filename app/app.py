# Untuk test github cli
#
# from PySide6.QtWidgets import QApplication
# from core.session import Session
# from views.auth.login_window import LoginWindow
# from views.main.main_window import MainWindow
# import sys
# 
# app = QApplication(sys.argv)
# 
# if Session.is_logged_in():
#     window = MainWindow()
# else:
#     window = LoginWindow()
# 
# window.show()
# sys.exit(app.exec())

import sys
import os

def main():
    from PySide6.QtWidgets import QApplication
    from core.session import Session
    from views.auth.login_window import LoginWindow
    from views.main.main_window import MainWindow

    app = QApplication(sys.argv)

    if Session.is_logged_in():
        window = MainWindow()
    else:
        window = LoginWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    # Kalau di CI, jangan jalankan GUI
    if os.environ.get("CI") == "true":
        print("Running in CI mode, GUI skipped")
    else:
        main()
