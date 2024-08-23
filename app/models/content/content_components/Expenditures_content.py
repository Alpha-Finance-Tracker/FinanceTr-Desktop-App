from PySide6.QtCharts import QChartView
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox
import requests
from PySide6.QtCharts import QChart, QPieSeries
from PySide6.QtCore import Qt
from dotenv import load_dotenv

from app.utils.auth_service import prepare_token_for_request

load_dotenv()

finance_service = 'http://127.0.0.1:8001'


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

        self.Monthly.clicked.connect(self.on_Monthly_clicked)
        self.Weekly.clicked.connect(self.on_Weekly_clicked)
        self.Quarter.clicked.connect(self.on_Quarter_clicked)
        self.Year.clicked.connect(self.on_Year_clicked)
        self.init_ui()

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

    def setCategoryExpenditureContent(self, chart):
        if isinstance(chart, QChart):
            self.category_chart.setChart(chart)

    def setTypeExpenditureContent(self, chart):
        if isinstance(chart, QChart):
            self.type_chart.setChart(chart)

    def setNameExpenditureContent(self, chart):
        if isinstance(chart, QChart):
            self.name_chart.setChart(chart)

    def request_Category_Expenditures(self, token, interval='Total'):
        headers = {'Authorization': f'Bearer {token}'}
        categories_url = f"{finance_service}/Finance_tracker/category_expenditures"
        data = {'interval': interval}
        try:
            categories_response = requests.get(categories_url, params=data, headers=headers)
            if categories_response.status_code == 200:
                categories_chart = self.expenditures_pie_chart(categories_response.json(), 'By Category')
                print(categories_response.json())
                self.setCategoryExpenditureContent(categories_chart)
            else:
                print(
                    f"Failed to load data. Categories status: {categories_response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")

    def request_Type_Expenditures(self, token, interval='Total'):
        headers = {'Authorization': f'Bearer {token}'}
        type_expenditures = f"{finance_service}/Finance_tracker/food_type_expenditures"
        data = {'interval': interval}
        try:
            foods_response = requests.get(type_expenditures, params=data, headers=headers)
            if foods_response.status_code == 200:
                types_chart = self.expenditures_pie_chart(foods_response.json(), 'By Type')
                self.setTypeExpenditureContent(types_chart)
            else:
                print(
                    f"Failed to load data. Categories status: {foods_response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")

    def request_Name_Expenditures(self, token, interval='Total'):
        headers = {'Authorization': f'Bearer {token}'}
        names = f"{finance_service}/Finance_tracker/food_name_expenditures"
        data = {'interval': interval}
        try:
            names_response = requests.get(names, params=data, headers=headers)
            if names_response.status_code == 200:
                names_chart = self.expenditures_pie_chart(names_response.json(), 'By Name')
                self.setNameExpenditureContent(names_chart)
            else:
                print(
                    f"Failed to load data. Categories status: {names_response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")

    def expenditures_handler(self):
        token = prepare_token_for_request()
        try:
            self.request_Category_Expenditures(token)
            self.request_Type_Expenditures(token)
            self.request_Name_Expenditures(token)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def expenditures_pie_chart(self, data, title):
        if title == "By Name":
            chart_pie = QPieSeries()

            for k, v in data.items():
                chart_slice = chart_pie.append(k, v)
                chart_slice.setLabel(f'{k}: {v}BGN')

            chart = QChart()
            chart.addSeries(chart_pie)
            chart.setTitle(title)
            chart.legend().setAlignment(Qt.AlignBottom)
            chart.legend().setVisible(True)

            self.combo_box.addItems([f"{k}: {v}BGN" for k, v in data.items()])
            self.combo_box.setMaxVisibleItems(1000)  # Set max visible items before scroll
            self.combo_box.setMinimumWidth(200)  # Adjust width as necessary
            return chart

        chart_pie = QPieSeries()

        for k, v in data.items():
            chart_slice = chart_pie.append(k, v)
            chart_slice.setLabel(f'{k}: {v}BGN')

        chart = QChart()
        chart.addSeries(chart_pie)
        chart.setTitle(title)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setVisible(True)

        return chart

    def on_Monthly_clicked(self):
        token = prepare_token_for_request()
        try:
            self.request_Category_Expenditures(token, interval='Month')
            self.request_Type_Expenditures(token, interval='Month')
            self.request_Name_Expenditures(token, interval='Month')

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def on_Weekly_clicked(self):
        token = prepare_token_for_request()
        try:
            self.request_Category_Expenditures(token, interval='Week')
            self.request_Type_Expenditures(token, interval='Week')
            self.request_Name_Expenditures(token, interval='Week')

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def on_Quarter_clicked(self):
        token = prepare_token_for_request()
        try:
            self.request_Category_Expenditures(token, interval='Quarter')
            self.request_Type_Expenditures(token, interval='Quarter')
            self.request_Name_Expenditures(token, interval='Quarter')

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def on_Year_clicked(self):
        token = prepare_token_for_request()
        try:
            self.request_Category_Expenditures(token, interval='Year')
            self.request_Type_Expenditures(token, interval='Year')
            self.request_Name_Expenditures(token, interval='Year')

        except Exception as e:
            print(f"An error occurred: {str(e)}")
