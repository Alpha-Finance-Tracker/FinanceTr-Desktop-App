from PySide6.QtWidgets import QWidget
from dotenv import load_dotenv

from app.models.user_interfaces.finance_tracker_user_interface import FinanceTrackerUserInterface


load_dotenv()
finance_service = 'http://127.0.0.1:8001'


class FinanceTrContent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = FinanceTrackerUserInterface()

        self.init_ui()


    def init_ui(self):
        layout = self.ui.init_ui()
        self.setLayout(layout)
