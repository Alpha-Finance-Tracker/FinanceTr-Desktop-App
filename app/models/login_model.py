from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
)
from PySide6.QtCore import Qt
import os
import requests
from dotenv import load_dotenv

load_dotenv()
login_service = os.getenv('LOGIN_SERVICE')


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(300, 150)

        self._token = None  # Private attribute to store the token

        # Create widgets
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password characters
        self.login_button = QPushButton("Login")

        # Layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.setLayout(self.layout)

        # Connect the button click event to the login method
        self.login_button.clicked.connect(self.login)

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, user_token):
        self._token = user_token  # Correctly set the private token attribute

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        data = {'username': username, 'password': password}
        result = requests.post(f"{login_service}/login", data=data)

        if result.status_code == 201:
            info = result.json()
            self.token = info['access_token']
            self.close()
        else:
            QMessageBox.warning(self, "Login", "Invalid username or password.")
