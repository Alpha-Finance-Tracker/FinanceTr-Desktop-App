from PySide6.QtCharts import QChartView
from PySide6.QtWidgets import QWidget, QVBoxLayout
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

        self.chart_view_1 = QChartView()
        self.chart_view_2 = QChartView()
        self.chart_view_3 = QChartView()

        charts_layout = QVBoxLayout()
        charts_layout.addWidget(self.chart_view_1)
        charts_layout.addWidget(self.chart_view_2)
        charts_layout.addWidget(self.chart_view_3)

        layout.addLayout(charts_layout)
        self.setLayout(layout)

    def setExpendituresContent(self, chart1, chart2, chart3):
        if isinstance(chart1, QChart):
            self.chart_view_1.setChart(chart1)
        if isinstance(chart2, QChart):
            self.chart_view_2.setChart(chart2)
        if isinstance(chart3, QChart):
            self.chart_view_3.setChart(chart3)

    def expenditures_handler(self):
        headers = {'Authorization': f'Bearer {retrieve_token()}'}
        categories_url = f"{finance_service}/Finance_tracker/category_expenditures"
        foods_url = f"{finance_service}/Finance_tracker/food_type_expenditures"
        foods_names_url = f"{finance_service}/Finance_tracker/food_name_expenditures"

        try:
            categories_response = requests.get(categories_url, headers=headers)
            foods_response = requests.get(foods_url, headers=headers)
            foods_names_response = requests.get(foods_names_url, headers=headers)

            if categories_response.status_code == 200 and foods_response.status_code == 200 and foods_names_response.status_code == 200:
                categories_chart = self.expenditures_pie_chart(categories_response.json(), 'By Category')
                food_chart = self.expenditures_pie_chart(foods_response.json(), 'By Type')
                food_name_chart = self.expenditures_pie_chart(foods_names_response.json(), 'By Name')
                self.setExpendituresContent(categories_chart, food_chart, food_name_chart)
            else:
                print(f"Failed to load data. Categories status: {categories_response.status_code}, Foods status: {foods_response.status_code}")


        except requests.RequestException as e:
            print(f"An error occurred: {str(e)}")


    def expenditures_pie_chart(self,data, title):
        chart_pie = QPieSeries()

        for k, v in data.items():
            slice = chart_pie.append(k, v)
            slice.setLabel(f'{k}: {v}BGN')

        chart = QChart()
        chart.addSeries(chart_pie)
        chart.setTitle(title)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setVisible(True)

        return chart
