import requests
from PySide6.QtCharts import QChart, QPieSeries
from PySide6.QtCore import Qt
import logging

finance_service = 'http://127.0.0.1:8001'

class ChartService:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'Bearer {token}'}

    def request_expenditures(self, endpoint, interval):
        url = f"{finance_service}/Finance_tracker/{endpoint}"
        params = {'interval': interval}
        try:
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Request failed for {url}: {e}")
            return None

    def create_pie_chart(self, data, title, combo_box=None):
        chart_pie = QPieSeries()
        for k, v in data.items():
            chart_slice = chart_pie.append(k, v)
            chart_slice.setLabel(f'{k}: {v}BGN')

        chart = QChart()
        chart.addSeries(chart_pie)
        chart.setTitle(title)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setVisible(True)

        if combo_box and title == "By Name":
            combo_box.addItems([f"{k}: {v}BGN" for k, v in data.items()])
            combo_box.setMaxVisibleItems(1000)
            combo_box.setMinimumWidth(200)

        return chart

    def update_combo_box(self, combo_box, data):
        combo_box.clear()
        combo_box.addItems([f"{k}: {v}BGN" for k, v in data.items()])
        combo_box.setMaxVisibleItems(1000)
        combo_box.setMinimumWidth(200)
