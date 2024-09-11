from PySide6.QtCharts import QChartView
from PySide6.QtWidgets import QWidget, QPushButton, QComboBox, QVBoxLayout

from app.models.buttons.expenditures_buttons import ExpendituresButtons


class ExpendituresUserInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons = ExpendituresButtons()
        self.category_chart = QChartView()
        self.type_chart = QChartView()
        self.name_chart = QChartView()
        self.combo_box = QComboBox()


    def init_ui(self):
        layout = QVBoxLayout()
        charts_layout = QVBoxLayout()
        charts_layout.addWidget(self.category_chart)
        charts_layout.addWidget(self.type_chart)
        charts_layout.addWidget(self.name_chart)
        charts_layout.addWidget(self.combo_box)
        charts_layout.addWidget(self.buttons.Monthly)
        charts_layout.addWidget(self.buttons.Weekly)
        charts_layout.addWidget(self.buttons.Quarter)
        charts_layout.addWidget(self.buttons.Year)
        layout.addLayout(charts_layout)

        return layout