import os

from PySide6.QtCharts import QPieSeries, QChart
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QPushButton, QFrame
import requests
from dotenv import load_dotenv

load_dotenv()
finance_service = os.getenv('FINANCE_SERVICE')
class Sidebar(QWidget):
    def __init__(self, content_area,token):
        super().__init__()
        self.content_area = content_area
        self._token = token
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a frame to hold the buttons
        self.sidebar_frame = QFrame()
        self.sidebar_frame.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
        frame_layout = QVBoxLayout(self.sidebar_frame)

        # Add 5 unique buttons to the frame
        buttons = [
            ("Expenditures", self.show_expenditures),
            ("K-receipts", self.show_reports),
            ("FinanceTr", self.show_settings),
            ("Profile", self.show_profile),
            ("Logout", self.show_logout),
        ]

        for name, handler in buttons:
            button = QPushButton(name)
            button.clicked.connect(handler)
            frame_layout.addWidget(button)

        layout.addWidget(self.sidebar_frame)
        self.setLayout(layout)

    def show_expenditures(self):
        data = {'token': self._token}
        categories_url = f"{finance_service}/Finance_tracker/category_expenditures"
        foods_url = f"{finance_service}/Finance_tracker/food_type_expenditures"
        foods_names_url = f"{finance_service}/Finance_tracker/food_name_expenditures"

        try:

            categories_response = requests.get(categories_url, params=data)
            foods_response = requests.get(foods_url, params=data)
            foods_names_response = requests.get(foods_names_url, params=data)

            if categories_response.status_code == 200 and foods_response.status_code == 200 and foods_names_response.status_code==200:
                categories_chart = self.expenditures_pie_chart(categories_response.json(),'By Category')
                food_chart = self.expenditures_pie_chart(foods_response.json(), 'By Type')
                food_name_chart = self.expenditures_pie_chart(foods_names_response.json(), 'By Name')
                self.content_area.setContent(categories_chart,food_chart,food_name_chart)
            else:
                # Detailed error messages
                error_message = f"Failed to load data. Categories status: {categories_response.status_code}, Foods status: {foods_response.status_code}"
                self.content_area.setContent(error_message)

        except requests.RequestException as e:
            # Handle network-related errors
            error_message = f"An error occurred: {str(e)}"
            self.content_area.setContent(error_message)

    def show_reports(self):
        self.content_area.setCurrentIndex(1)

    def show_settings(self):
        self.content_area.setCurrentIndex(2)

    def show_profile(self):
        self.content_area.setCurrentIndex(3)

    def show_logout(self):
        self.content_area.setCurrentIndex(4)


    def expenditures_pie_chart(self,data,title):
        chart_pie = QPieSeries()

        for k,v in data.items():
            slice = chart_pie.append(k, v)

            slice.setLabel(f'{k}: {v}BGN')

        chart = QChart()
        chart.addSeries(chart_pie)
        chart.setTitle(title)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setVisible(True)

        return chart


