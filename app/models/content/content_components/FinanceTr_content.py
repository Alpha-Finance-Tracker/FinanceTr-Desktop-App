from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QDateEdit, QPushButton, QHBoxLayout
from PySide6.QtCharts import QChartView, QChart

class FinanceTrContent(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        self.category_input = QLineEdit()
        self.type_input = QLineEdit()
        self.date_input = QDateEdit()

        form_layout.addRow('Name:', self.name_input)
        form_layout.addRow('Price:', self.price_input)
        form_layout.addRow('Category:', self.category_input)
        form_layout.addRow('Type:', self.type_input)
        form_layout.addRow('Date:', self.date_input)

        submit_button = QPushButton('Submit')
        # connect submit_button to a method for handling form submission
        submit_button.clicked.connect(self.submit_data)

        layout.addLayout(form_layout)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit_data(self):
        # Handle data submission logic here
        pass