from PySide6.QtWidgets import QWidget
from app.models.data_streams.expenditures_ds import ExpendituresDataStream
from app.models.user_interfaces.expenditures_user_interface import ExpendituresUserInterface
from app.utils.auth_service import prepare_token_for_request


class ExpendituresContent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ExpendituresUserInterface()
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        layout = self.ui.init_ui()
        self.setLayout(layout)

    def connect_signals(self):
        self.ui.buttons.Monthly.clicked.connect(lambda: self.update_expenditures('Month'))
        self.ui.buttons.Weekly.clicked.connect(lambda: self.update_expenditures('Week'))
        self.ui.buttons.Quarter.clicked.connect(lambda: self.update_expenditures('Quarter'))
        self.ui.buttons.Year.clicked.connect(lambda: self.update_expenditures('Year'))

    def update_expenditures(self, interval):
        token = prepare_token_for_request()

        service = ExpendituresDataStream(token,
                                         self.ui.category_chart,
                                         self.ui.type_chart,
                                         self.ui.name_chart,
                                         self.ui.combo_box)

        futures = service.futures(interval)
        service.display(futures)
