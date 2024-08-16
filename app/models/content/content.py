from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget, QFormLayout, QLineEdit, QDateEdit, QPushButton
from PySide6.QtCharts import QChartView, QChart

from app.models.content.content_components.Expenditures_content import ExpendituresContent
from app.models.content.content_components.FinanceTr_content import FinanceTrContent


class Content(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.finance_tr_content = FinanceTrContent()
        self.expenditures_content = ExpendituresContent()

        self.addWidget(self.expenditures_content)  # Index 0
        self.addWidget(self.finance_tr_content)


    def show_expenditures(self,token):
        self.expenditures_content.expenditures_handler(token)
        self.setCurrentIndex(0)



    def show_financeTR(self,token):
            self.setCurrentIndex(1)


    #
    #     def show_settings(self):
    #         self.content_area.setCurrentIndex(2)
    #
    #     def show_profile(self):
    #         self.content_area.setCurrentIndex(3)
    #
    #     def show_logout(self):
    #         self.content_area.setCurrentIndex(4)