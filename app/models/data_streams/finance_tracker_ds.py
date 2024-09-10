import requests
from PySide6.QtCore import QDate
from app.models.base_models.data_stream import DataStream

finance_service = 'http://127.0.0.1:8001'

class FinanceTrackerDs(DataStream):

    def __init__(self, token):
        super().__init__()

        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.url = f"{finance_service}/Finance_tracker/update"

    def request(self,data):
        return requests.post(self.url, headers=self.headers, json=data)

    def display(self,data):
        if data.status_code == 200:
            return True
        else:
            return False