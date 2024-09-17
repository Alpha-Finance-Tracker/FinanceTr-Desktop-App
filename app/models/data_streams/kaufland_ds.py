import os

import requests

from app.models.base_models.data_stream import DataStream
finance_service = 'http://127.0.0.1:8001'

class KauflandDs(DataStream):

    def __init__(self,token):
        self.token = token
        self.headers = {'Authorization': f'Bearer {token}'}
        self.url = f"{finance_service}/Finance_tracker/kaufland_receipt"
        self.file_name = None


    def request(self,data):
        self.file_name = data['file']

        if not self.file_name:
            raise 'No file to upload.'


        try:
            with open(self.file_name, 'rb') as file:
                files = {'image': (os.path.basename(self.file_name), file)}

                response = requests.post(self.url, headers=self.headers, files=files, params={'date':data['date']})
                response.raise_for_status()
                return response

        except requests.RequestException as e:
            raise e

    def display(self,data):
        if data:
            return f'Upload Successful: {data.status_code}'
        else:
            return f'Upload Failed: {data.status_code}'
