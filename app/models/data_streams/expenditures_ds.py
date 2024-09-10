import logging

import requests
from app.models.base_models.data_stream import DataStream
from app.models.charts.charts import ChartService
from concurrent.futures import ThreadPoolExecutor

finance_service = 'http://127.0.0.1:8001'
class ExpendituresDataStream(DataStream):

    def __init__(self,token,category_chart,type_chart,name_chart,combo_box):
        self.category_chart = category_chart
        self.type_chart = type_chart
        self.name_chart = name_chart
        self.combo_box = combo_box

        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.url = f"{finance_service}/Finance_tracker/view_expenditures"
        self.executor = ThreadPoolExecutor(max_workers=3)

    def request(self,data):

        try:
            response = requests.post(self.url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Request failed for {self.url}: {e}")
            return None

    def display(self,data):
        chart_service = ChartService()

        for key, future in data.items():
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

    def futures(self,interval):
        category_data = {'interval': interval, 'column_type': 'category', 'category': 'Optional'}
        type_data = {'interval': interval, 'column_type': 'type', 'category': 'Food'}
        name_data = {'interval': interval, 'column_type': 'name', 'category': 'Optional'}

        futures = {
            'category': self.executor.submit(self.request, category_data),
            'type': self.executor.submit(self.request, type_data),
            'name': self.executor.submit(self.request, name_data),
        }

        return futures