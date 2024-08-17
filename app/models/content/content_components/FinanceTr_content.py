import os
from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QCalendarWidget, QPushButton, \
    QHBoxLayout, QMessageBox, QLabel
from PySide6.QtCore import QDate, QSize
from PySide6.QtGui import QIcon
import requests
from dotenv import load_dotenv

load_dotenv()
finance_service = os.getenv('FINANCE_SERVICE')

class FinanceTrContent(QWidget):
    def __init__(self, token):
        self.token = token
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()

        # Calendar for Date Input
        self.date_input = QCalendarWidget()
        self.date_input.setGridVisible(True)
        self.date_input.setSelectedDate(QDate.currentDate())

        # Labels
        self.category_label = QLabel("Category:")
        self.type_label = QLabel("Type:")

        self.category_buttons = {}
        self.type_buttons = {}

        # Example categories
        self.add_category_button('Food', 'images/food.png')
        self.add_category_button('Transport', 'images/transportation.png')
        self.add_category_button('Health', 'images/health.jpg')
        self.add_category_button('Entertainment', 'images/entertainment.png')
        self.add_category_button('Home', 'images/home.png')
        self.add_category_button('Sport', 'images/sport.jpg')

        # Example types
        self.add_type_button('Animal', 'images/types/food/animal.jpg', categories=['Food'])
        self.add_type_button('Dairy', 'images/types/food/dairy.png', categories=['Food'])
        self.add_type_button('Nuts', 'images/types/food/nuts.png', categories=['Food'])
        self.add_type_button('Vegetables', 'images/types/food/vegetables.png', categories=['Food'])
        self.add_type_button('Beverages', 'images/types/food/beverages.png', categories=['Food'])

        form_layout.addRow('Name:', self.name_input)
        form_layout.addRow('Price:', self.price_input)
        form_layout.addRow('Date:', self.date_input)

        # Adding Category buttons
        category_layout = QHBoxLayout()
        category_layout.addWidget(self.category_label)
        for button in self.category_buttons.values():
            category_layout.addWidget(button)
        form_layout.addRow(category_layout)

        # Adding Type buttons
        self.type_layout = QHBoxLayout()
        self.type_layout.addWidget(self.type_label)
        form_layout.addRow(self.type_layout)

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.submit_data)

        layout.addLayout(form_layout)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def add_category_button(self, name, image_path):
        button = QPushButton(self)
        button.setIcon(QIcon(image_path))
        button.setIconSize(QSize(64, 64))
        button.setCheckable(True)
        button.clicked.connect(lambda: self.select_category(name))
        self.category_buttons[name] = button

    def add_type_button(self, name, image_path, categories):
        button = QPushButton(self)
        button.setIcon(QIcon(image_path))
        button.setIconSize(QSize(64, 64))
        button.setCheckable(True)
        button.clicked.connect(lambda: self.select_type(name))
        button.hide()  # Initially hide all type buttons
        self.type_buttons[name] = {'button': button, 'categories': categories}

    def select_type(self, type_name):
        for btn_name, button_info in self.type_buttons.items():
            button_info['button'].setChecked(btn_name == type_name)
        self.selected_type = type_name

    def select_category(self, category_name):
        for btn_name, button in self.category_buttons.items():
            button.setChecked(btn_name == category_name)
        self.selected_category = category_name

        # Clear existing type buttons from layout
        for i in reversed(range(self.type_layout.count())):
            widget = self.type_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Show only the type buttons related to the selected category
        for button_info in self.type_buttons.values():
            if category_name in button_info['categories']:
                button_info['button'].show()
                self.type_layout.addWidget(button_info['button'])
            else:
                button_info['button'].hide()

    def submit_data(self):
        update_url = f"{finance_service}/Finance_tracker/update"
        data = {
            'token': self.token,
            'name': self.name_input.text(),
            'price': self.price_input.text(),
            'category': self.selected_category,
            'type': self.selected_type,
            'date': self.date_input.selectedDate().toString('dd.MM.yyyy')
        }

        update_response = requests.put(update_url, params=data)
        if update_response.status_code == 200:
            self.name_input.clear()
            self.price_input.clear()
            self.date_input.setSelectedDate(QDate.currentDate())

            # Uncheck all buttons and hide types
            for button in self.type_buttons.values():
                button['button'].setChecked(False)
                button['button'].hide()
            for button in self.category_buttons.values():
                button.setChecked(False)

            QMessageBox.information(self, "Success", "Registered successfully!")
        else:
            QMessageBox.information(self, "Fail", "Update failed!")
