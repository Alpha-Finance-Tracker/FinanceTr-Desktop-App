import os

import requests
from PySide6.QtCharts import QChartView, QChart
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QStackedWidget, QHBoxLayout
from dotenv import load_dotenv


class Content(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Initialize widgets for displaying charts
        self.chart_view_1 = QChartView()
        self.chart_view_2 = QChartView()
        self.chart_view_3 = QChartView()
        # Set up layout
        layout = QHBoxLayout()
        layout.addWidget(self.chart_view_1)
        layout.addWidget(self.chart_view_2)
        layout.addWidget(self.chart_view_3)

        container = QWidget()
        container.setLayout(layout)

        # Add container widget to the stacked widget
        self.addWidget(container)

    def setContent(self, chart1, chart2,chart3):
        # Ensure chart1 and chart2 are QChart objects
        if isinstance(chart1, QChart):
            self.chart_view_1.setChart(chart1)
        if isinstance(chart2, QChart):
            self.chart_view_2.setChart(chart2)
        if isinstance(chart3, QChart):
            self.chart_view_3.setChart(chart3)

        # Show the widget containing the charts
        self.setCurrentIndex(0)