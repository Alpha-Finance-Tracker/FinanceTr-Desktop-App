import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from app.models.dashboard.Dashboard import Dashboard
from app.models.login.login_model import LoginWidget

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("images/app_icon.png"))

login_widget = LoginWidget()
login_widget.show()
app.exec()
token = login_widget.token

if token:
    main_window = Dashboard(token)
    main_window.show()
    app.exec()