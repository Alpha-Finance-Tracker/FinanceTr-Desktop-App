import sys

from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QStackedWidget, QApplication

from app.models.Dashboard import Dashboard
from app.models.Main_window_model import MainWindow
from app.models.login_model import LoginWidget
from app.models.register_expenditures import CircleWidget, ExpenditureDetail

app = QApplication(sys.argv)


# login_widget = LoginWidget()
# login_widget.show()
# app.exec()
# token = login_widget.token
#
# if token:
main_window = Dashboard(None)
main_window.show()
app.exec()