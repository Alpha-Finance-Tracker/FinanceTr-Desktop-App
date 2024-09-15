from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QVBoxLayout, QLineEdit, QPushButton, QLabel, QSpacerItem, QSizePolicy, QWidget
)
from PySide6.QtCore import Qt
import os


class LoginUserInterface(QWidget):
    """
    This class inherits from QWidget and sets up the visual layout and UI components
    for the login screen, including input fields, buttons, and background.
    """

    def __init__(self):
        super().__init__()

        # Initialize UI components
        self.background_label = QLabel(self)
        self.overlay_widget = QWidget(self)
        self.username_label = QLabel("Username:", self.overlay_widget)
        self.password_label = QLabel("Password:", self.overlay_widget)
        self.username_input = QLineEdit(self.overlay_widget)
        self.password_input = QLineEdit(self.overlay_widget)
        self.login_button = QPushButton("Login", self.overlay_widget)


    def init_ui(self):
        """
        Sets up the layout for the login UI. This method creates and returns the layout
        which will be used by the main LoginWidget class.
        """
        layout = QVBoxLayout(self.overlay_widget)

        # Load the background image
        self.load_background_image()

        # Style username and password fields
        self.username_label.setStyleSheet("color: #ADD8E6;")
        self.username_input.setStyleSheet("color: #ADD8E6;")
        self.username_input.setFixedWidth(200)

        self.password_label.setStyleSheet("color: #ADD8E6;")
        self.password_input.setStyleSheet("color: #ADD8E6;")
        self.password_input.setFixedWidth(200)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button.setStyleSheet("color: #ADD8E6;")

        # Add widgets to the layout
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        layout.setAlignment(Qt.AlignCenter)
        return

    def load_background_image(self):
        """
        Loads the background image for the login widget.
        """
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
        """
        Override resizeEvent to handle background image resizing when the window changes size.
        """
        super().resizeEvent(event)
        if self.background_label.pixmap():
            scaled_pixmap = self.background_label
