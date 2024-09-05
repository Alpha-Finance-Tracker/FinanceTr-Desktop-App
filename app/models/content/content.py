from PySide6.QtWidgets import QStackedWidget
from app.models.content.content_components.Expenditures_content import ExpendituresContent
from app.models.content.content_components.FinanceTr_content import FinanceTrContent
from app.models.content.content_components.Home_content import Home
from app.models.content.content_components.Stock_content import StockContent
from app.models.content.content_components.kaufland_receipt_content import KauflandReceiptsContent
from app.models.content.content_components.lidl_receipt_content import LidlReceiptsContent

class Content(QStackedWidget):
    CONTENT = {
        "expenditures": ExpendituresContent,
        "finance_tr": FinanceTrContent,
        "home": Home,
        "kaufland_receipts": KauflandReceiptsContent,
        "lidl_receipts": LidlReceiptsContent,
        # 'stock':StockContent,
    }

    def __init__(self):
        super().__init__()
        self.content = self.create_content_pages()
        self.setup_content()

    def create_content_pages(self):
        return {key: cls() for key, cls in self.CONTENT.items()}

    def setup_content(self):
        for section in self.content.values():
            self.addWidget(section)

    def show_expenditures(self):
        self.show_page("expenditures")
        self.content["expenditures"].update_expenditures('Total')

    def show_financeTR(self):
        self.show_page("finance_tr")

    def show_home(self):
        self.show_page("home")

    def show_receipt_menu(self):
        self.show_page("kaufland_receipts")

    def show_stock_menu(self):
        self.show_page('stock')

    def show_page(self, page_key):
        self.setCurrentWidget(self.content[page_key])
