from PySide6.QtWidgets import QStackedWidget

from app.models.content.content_components.Expenditures_content import ExpendituresContent
from app.models.content.content_components.FinanceTr_content import FinanceTrContent
from app.models.content.content_components.Home_content import Home
from app.models.content.content_components.kaufland_receipt_content import KauflandReceiptsContent
from app.models.content.content_components.lidl_receipt_content import LidlReceiptsContent


class Content(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.home_content = Home()
        self.finance_tr_content = FinanceTrContent()
        self.expenditures_content = ExpendituresContent()
        self.kaufland_receipts_content = KauflandReceiptsContent()
        self.lidl_receipts_content = LidlReceiptsContent()

        self.addWidget(self.expenditures_content)
        self.addWidget(self.finance_tr_content)
        self.addWidget(self.home_content)
        self.addWidget(self.kaufland_receipts_content)
        self.addWidget(self.lidl_receipts_content)

    def show_expenditures(self):
        self.expenditures_content.update_expenditures('Total')
        self.setCurrentIndex(0)

    def show_financeTR(self):
        self.setCurrentIndex(1)

    def show_home(self):
        self.setCurrentIndex(2)

    def show_receipt_menu(self):
        self.setCurrentIndex(3)

    #
    #     def show_settings(self):
    #         self.content_area.setCurrentIndex(2)
    #
    #     def show_profile(self):
    #         self.content_area.setCurrentIndex(3)
    #
    #     def show_logout(self):
    #         self.content_area.setCurrentIndex(4)
