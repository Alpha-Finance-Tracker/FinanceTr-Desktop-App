from PySide6.QtCore import  QDate
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QFormLayout, QLabel, QLineEdit, QCalendarWidget, \
    QWidget, QMessageBox

from app.models.buttons.finance_tracker_buttons import FinanceTrackerButtons
from app.models.data_streams.finance_tracker_ds import FinanceTrackerDs
from app.utils.auth_service import prepare_token_for_request


class FinanceTrackerUserInterface(QWidget):

    def __init__(self):
        super().__init__()

        # Input Fields
        self.name_input = QLineEdit()
        self.price_input = QLineEdit()

        # Calendar for Date Input
        self.date_input = QCalendarWidget()
        self.date_input.setGridVisible(True)
        self.date_input.setSelectedDate(QDate.currentDate())

        # Labels
        self.category_label = QLabel("Category:")
        self.type_label = QLabel("Type:")


        # Grid
        self.type_layout = QHBoxLayout()

        # Buttons
        self.buttons = FinanceTrackerButtons(self.type_layout)

    def init_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.buttons.set_category_buttons()
        self.buttons.set_type_buttons()

        form_layout.addRow('Name:', self.name_input)
        form_layout.addRow('Price:', self.price_input)
        form_layout.addRow('Date:', self.date_input)

        category_layout = QHBoxLayout()

        category_layout.addWidget(self.category_label)
        for button in self.buttons.category_buttons.values():
            category_layout.addWidget(button)
        form_layout.addRow(category_layout)


        self.type_layout.addWidget(self.type_label)
        form_layout.addRow(self.type_layout)

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.submit_data)

        layout.addLayout(form_layout)
        layout.addWidget(submit_button)

        return layout

    def submit_data(self):
        token = prepare_token_for_request()
        service = FinanceTrackerDs(token)

        data = {
            'name': self.name_input.text(),
            'price': self.price_input.text().replace(',', '.'),
            'category': self.buttons.selected_category,
            'expenditure_type': self.buttons.selected_type,
            'date': self.date_input.selectedDate().toString('dd.MM.yyyy')
        }

        response = service.display(service.request(data))
        self.display_response(response)

    def display_response(self,response):
        if response:
            self.name_input.clear()
            self.price_input.clear()
            self.date_input.setSelectedDate(QDate.currentDate())
            for button in self.buttons.type_buttons.values():
                button['button'].setChecked(False)
                button['button'].hide()
            for button in self.buttons.category_buttons.values():
                button.setChecked(False)
            QMessageBox.information(self, "Success", "Registered successfully!")
        else:
            QMessageBox.information(self, "Fail", "Registration unsuccessful!")
