from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QSpacerItem, QSizePolicy
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

        # Initialize background label
        self.background_label = QLabel(self)
        self.load_background_image()

        # Initialize overlay widget
        self.overlay_widget = QWidget(self)
        self.overlay_widget.setStyleSheet("background: transparent;")
        self.overlay_layout = QVBoxLayout(self.overlay_widget)

        # Create widgets
        self.username_label = QLabel("Username:", self.overlay_widget)
        self.password_label = QLabel("Password:", self.overlay_widget)
        self.login_button = QPushButton("Login", self.overlay_widget)


        self.username_input = QLineEdit(self.overlay_widget)
        self.username_label.setStyleSheet("color: #ADD8E6;")
        self.username_input.setStyleSheet("color: #ADD8E6;")
        self.username_input.setFixedWidth(200)  # Set fixed width for username input

        self.password_input = QLineEdit(self.overlay_widget)
        self.password_label.setStyleSheet("color: #ADD8E6;")
        self.password_input.setStyleSheet("color: #ADD8E6;")
        self.password_input.setFixedWidth(200)  # Set fixed width for password input
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password characters


        self.login_button = QPushButton("Login", self.overlay_widget)
        self.login_button.setStyleSheet("color: #ADD8E6;")


        # Add widgets to the overlay layout
        self.overlay_layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Spacer to push content down
        self.overlay_layout.addWidget(self.username_label)
        self.overlay_layout.addWidget(self.username_input)
        self.overlay_layout.addWidget(self.password_label)
        self.overlay_layout.addWidget(self.password_input)
        self.overlay_layout.addWidget(self.login_button)

        self.overlay_layout.setAlignment(Qt.AlignCenter)

        # Connect the button click event
        self.login_button.clicked.connect(self.login)

    def load_background_image(self):
        """Load and set the background image."""
        image_path = 'images/login/login_background.jpg'
        if os.path.isfile(image_path):
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.background_label.setPixmap(scaled_pixmap)
            self.background_label.setAlignment(Qt.AlignCenter)
            self.background_label.setGeometry(self.rect())  # Ensure it covers the full screen
        else:
            print(f"Error: File '{image_path}' not found.")

    def resizeEvent(self, event):
        """Reposition and resize the background image and overlay widget when the window is resized."""
        super().resizeEvent(event)
        if self.background_label.pixmap():
            scaled_pixmap = self.background_label.pixmap().scaled(self.size(), Qt.KeepAspectRatioByExpanding,
                                                                  Qt.SmoothTransformation)
            self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setGeometry(self.rect())  # Ensure it covers the full screen
        self.overlay_widget.resize(self.size())

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        data = {'username': username, 'password': password}
        try:
            result = requests.post(f"{login_service}/login", data=data)
            if result.status_code == 201:
                info = result.json()
                self.token = info['access_token']
                self.close()
            else:
                QMessageBox.warning(self, "Login", "Invalid username or password.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Login", f"An error occurred: {e}")

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, user_token):
        self._token = user_token
