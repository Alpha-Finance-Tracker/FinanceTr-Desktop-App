from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
import os
import requests

from app.models.data_streams.login_ds import LoginDatastream

login_service = 'http://127.0.0.1:8000'

class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.logged = None
        self.login_service = LoginDatastream()
        self.setWindowTitle("Login")

        self.background_label = QLabel(self)
        self.load_background_image()


        self.overlay_widget = QWidget(self)
        self.overlay_widget.setStyleSheet("background: transparent;")
        self.overlay_layout = QVBoxLayout(self.overlay_widget)


        self.username_label = QLabel("Username:", self.overlay_widget)
        self.password_label = QLabel("Password:", self.overlay_widget)
        self.login_button = QPushButton("Login", self.overlay_widget)

        self.username_input = QLineEdit(self.overlay_widget)
        self.username_label.setStyleSheet("color: #ADD8E6;")
        self.username_input.setStyleSheet("color: #ADD8E6;")
        self.username_input.setFixedWidth(200)

        self.password_input = QLineEdit(self.overlay_widget)
        self.password_label.setStyleSheet("color: #ADD8E6;")
        self.password_input.setStyleSheet("color: #ADD8E6;")
        self.password_input.setFixedWidth(200)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self.overlay_widget)
        self.login_button.setStyleSheet("color: #ADD8E6;")


        self.overlay_layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.overlay_layout.addWidget(self.username_label)
        self.overlay_layout.addWidget(self.username_input)
        self.overlay_layout.addWidget(self.password_label)
        self.overlay_layout.addWidget(self.password_input)
        self.overlay_layout.addWidget(self.login_button)

        self.overlay_layout.setAlignment(Qt.AlignCenter)


        self.login_button.clicked.connect(self.login)

    def load_background_image(self):

        image_path = 'images/login/login_background.jpg'
        if os.path.isfile(image_path):
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            self.background_label.setPixmap(scaled_pixmap)
            self.background_label.setAlignment(Qt.AlignCenter)
            self.background_label.setGeometry(self.rect())
        else:
            print(f"Error: File '{image_path}' not found.")

    def resizeEvent(self, event):

        super().resizeEvent(event)
        if self.background_label.pixmap():
            scaled_pixmap = self.background_label.pixmap().scaled(self.size(), Qt.KeepAspectRatioByExpanding,
                                                                  Qt.SmoothTransformation)
            self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setGeometry(self.rect())
        self.overlay_widget.resize(self.size())

    def login(self):

        data = {'username': self.username_input.text(), 'password': self.password_input.text()}

        try:
            response = self.login_service.request(data)
            if self.login_service.display(response):
                self.logged = True
                self.close()
            else:
                QMessageBox.warning(self, "Login", "Invalid username or password.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Login", f"An error occurred: {e}")
