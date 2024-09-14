import requests

from app.models.base_models.data_stream import DataStream
from app.utils.auth_service import save_token

login_service = 'http://127.0.0.1:8000'
class LoginDatastream(DataStream):

    def __init__(self):
        self.logged = False


    def request(self,data):
        response =  requests.post(f"{login_service}/login", data=data)
        if response.status_code == 200:
            save_token(response.json()['access_token'], 'FinanceTr_Access_token')
            save_token(response.json()['refresh_token'], 'FinanceTr_Refresh_token')
            self.logged = True

        return response

    def display(self,data):
        return True if data.status_code == 200 else False

