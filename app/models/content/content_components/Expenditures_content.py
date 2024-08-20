from PySide6.QtCharts import QChartView
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
import os

import requests
from PySide6.QtCharts import QChart, QPieSeries
from PySide6.QtCore import Qt
from dotenv import load_dotenv

from app.utils.auth_service import retrieve_token

load_dotenv()
finance_service = os.getenv('FINANCE_TR_SERVICE')


class ExpendituresContent(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.Monthly = QPushButton("Monthly")
        self.Weekly = QPushButton("Weekly")
        self.Quarter = QPushButton("Quarter")
        self.Year = QPushButton('Year')
        self.Total = QPushButton('Total')

        self.Monthly.clicked.connect(self.on_Monthly_clicked())
        self.Weekly.clicked.connect(self.on_Weekly_clicked())
        self.Quarter.clicked.connect(self.on_Quarter_clicked())
        self.Year.clicked.connect(self.on_Year_clicked())
        self.Total.clicked.connect(self.on_Total_clicked())

        self.category_chart = QChartView()
        self.type_chart = QChartView()
        self.name_chart = QChartView()

        charts_layout = QVBoxLayout()

        charts_layout.addWidget(self.category_chart)
        charts_layout.addWidget(self.type_chart)
        charts_layout.addWidget(self.name_chart)
        charts_layout.addWidget(self.Monthly)
        charts_layout.addWidget(self.Weekly)
        charts_layout.addWidget(self.Quarter)
        charts_layout.addWidget(self.Year)
        charts_layout.addWidget(self.Total)

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

    def request_Category_Expenditures(self, token, interval=None):
        headers = {'Authorization': f'Bearer {token}'}
        categories_url = f"{finance_service}/Finance_tracker/category_expenditures"
        try:
            categories_response = requests.get(categories_url, headers=headers)
            if categories_response.status_code == 200:
                categories_chart = self.expenditures_pie_chart(categories_response.json(), 'By Category')
                self.setCategoryExpenditureContent(categories_chart)
            else:
                print(
                    f"Failed to load data. Categories status: {categories_response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")

    def request_Type_Expenditures(self, token, interval=None):
        headers = {'Authorization': f'Bearer {token}'}
        type_expenditures = f"{finance_service}/Finance_tracker/food_type_expenditures"
        try:
            foods_response = requests.get(type_expenditures, headers=headers)
            if foods_response.status_code == 200:
                types_chart = self.expenditures_pie_chart(foods_response.json(), 'By Type')
                self.setTypeExpenditureContent(types_chart)
            else:
                print(
                    f"Failed to load data. Categories status: {foods_response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")

    def request_Name_Expenditures(self, token, interval=None):
        headers = {'Authorization': f'Bearer {token}'}
        names = f"{finance_service}/Finance_tracker/food_name_expenditures"
        try:
            names_response = requests.get(names, headers=headers)
            if names_response.status_code == 200:
                names_chart = self.expenditures_pie_chart(names_response.json(), 'By Name')
                self.setNameExpenditureContent(names_chart)
            else:
                print(
                    f"Failed to load data. Categories status: {names_response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")

    def expenditures_handler(self):
        token = retrieve_token()
        try:
            self.request_Category_Expenditures(token)
            self.request_Type_Expenditures(token)
            self.request_Name_Expenditures(token)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def expenditures_pie_chart(self, data, title):
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
        token = retrieve_token()
        try:
            self.request_Category_Expenditures(token)
            self.request_Type_Expenditures(token)
            self.request_Name_Expenditures(token)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def on_Weekly_clicked(self):
        token = retrieve_token()
        try:
            self.request_Category_Expenditures(token)
            self.request_Type_Expenditures(token)
            self.request_Name_Expenditures(token)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def on_Quarter_clicked(self):
        token = retrieve_token()
        try:
            self.request_Category_Expenditures(token)
            self.request_Type_Expenditures(token)
            self.request_Name_Expenditures(token)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def on_Year_clicked(self):
        token = retrieve_token()
        try:
            self.request_Category_Expenditures(token)
            self.request_Type_Expenditures(token)
            self.request_Name_Expenditures(token)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def on_Total_clicked(self):
        token = retrieve_token()
        try:
            self.request_Category_Expenditures(token)
            self.request_Type_Expenditures(token)
            self.request_Name_Expenditures(token)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
