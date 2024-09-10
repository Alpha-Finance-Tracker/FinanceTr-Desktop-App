from PySide6.QtCharts import QChartView
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox
from app.models.data_streams.expenditures_ds import ExpendituresDataStream
from app.utils.auth_service import prepare_token_for_request


class ExpendituresContent(QWidget):
    def __init__(self):
        super().__init__()
        self.Monthly = QPushButton("Monthly")
        self.Weekly = QPushButton("Weekly")
        self.Quarter = QPushButton("Quarter")
        self.Year = QPushButton('Year')

        self.category_chart = QChartView()
        self.type_chart = QChartView()
        self.name_chart = QChartView()
        self.combo_box = QComboBox()
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        layout = QVBoxLayout()
        charts_layout = QVBoxLayout()
        charts_layout.addWidget(self.category_chart)
        charts_layout.addWidget(self.type_chart)
        charts_layout.addWidget(self.name_chart)
        charts_layout.addWidget(self.combo_box)
        charts_layout.addWidget(self.Monthly)
        charts_layout.addWidget(self.Weekly)
        charts_layout.addWidget(self.Quarter)
        charts_layout.addWidget(self.Year)
        layout.addLayout(charts_layout)
        self.setLayout(layout)

    def connect_signals(self):
        self.Monthly.clicked.connect(lambda: self.update_expenditures('Month'))
        self.Weekly.clicked.connect(lambda: self.update_expenditures('Week'))
        self.Quarter.clicked.connect(lambda: self.update_expenditures('Quarter'))
        self.Year.clicked.connect(lambda: self.update_expenditures('Year'))

    def update_expenditures(self, interval):
        token = prepare_token_for_request()

        service = ExpendituresDataStream(token,
                                         self.category_chart,
                                         self.type_chart,
                                         self.name_chart,
                                         self.combo_box)

        futures = service.futures(interval)
        service.display(futures)
