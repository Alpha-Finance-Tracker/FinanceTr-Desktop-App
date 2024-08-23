import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication


from app.models.dashboard.Dashboard import Dashboard
from app.models.login.login_model import LoginWidget
from app.utils.auth_service import retrieve_token, check_if_login_is_needed

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("images/app_icon.png"))

# import sys
#
# # Redirect stdout and stderr to files
# sys.stdout = open('output.log', 'w')
# sys.stderr = open('errors.log', 'w')



def start_app():
    check = check_if_login_is_needed()

    if check == False:
        main_window = Dashboard()
        main_window.show()
        app.exec()
    else:
        login_widget = LoginWidget()
        login_widget.show()
        app.exec()

        if login_widget.logged == True:
            main_window = Dashboard()
            main_window.show()
            app.exec()




start_app()