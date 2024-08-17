from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget, QFormLayout, QLineEdit, QDateEdit, QPushButton
from PySide6.QtCharts import QChartView, QChart

from app.models.content.content_components.Expenditures_content import ExpendituresContent
from app.models.content.content_components.FinanceTr_content import FinanceTrContent
from app.models.content.content_components.Home_content import Home


class Content(QStackedWidget):
    def __init__(self,token):
        super().__init__()
        self.token = token
        self.home_content = Home()
        self.finance_tr_content = FinanceTrContent(self.token)
        self.expenditures_content = ExpendituresContent(self.token)

        self.addWidget(self.expenditures_content)
        self.addWidget(self.finance_tr_content)
        self.addWidget(self.home_content)


    def show_expenditures(self):
        self.expenditures_content.expenditures_handler()
        self.setCurrentIndex(0)



    def show_financeTR(self):
        self.setCurrentIndex(1)


    def show_home(self):
        self.setCurrentIndex(2)


    #
    #     def show_settings(self):
    #         self.content_area.setCurrentIndex(2)
    #
    #     def show_profile(self):
    #         self.content_area.setCurrentIndex(3)
    #
    #     def show_logout(self):
    #         self.content_area.setCurrentIndex(4)