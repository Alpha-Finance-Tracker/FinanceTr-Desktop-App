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


if login_widget.logged == True:
    main_window = Dashboard()
    main_window.show()
    app.exec()