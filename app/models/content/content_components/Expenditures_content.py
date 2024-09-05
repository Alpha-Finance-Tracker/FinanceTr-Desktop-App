from PySide6.QtCharts import QChartView
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox

from concurrent.futures import ThreadPoolExecutor

from app.models.charts.charts import ChartService
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

        self.executor = ThreadPoolExecutor(max_workers=3)

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
        chart_service = ChartService(token)


        category_data = {'interval':interval,'column_type':'category','category':'Optional'}
        type_data = {'interval':interval,'column_type':'type','category':'Food'}
        name_data = {'interval':interval,'column_type':'name','category':'Optional'}

        futures = {
            'category': self.executor.submit(chart_service.request_expenditures, category_data),
            'type': self.executor.submit(chart_service.request_expenditures, type_data),
            'name': self.executor.submit(chart_service.request_expenditures, name_data),
        }

        for key, future in futures.items():
            data = future.result()
            if data:
                chart = chart_service.create_pie_chart(data, f'By {key.capitalize()}')
                if key == 'category':
                    self.category_chart.setChart(chart)
                elif key == 'type':
                    self.type_chart.setChart(chart)
                elif key == 'name':
                    self.name_chart.setChart(chart)
                    chart_service.update_combo_box(self.combo_box, data)
