import os
import requests
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QCalendarWidget
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QDate, QCoreApplication
from dotenv import load_dotenv

from app.models.data_streams.kaufland_ds import KauflandDs
from app.models.user_interfaces.kaufland_user_interface import KauflandUserInterface
from app.utils.auth_service import prepare_token_for_request

load_dotenv()
finance_service = 'http://127.0.0.1:8001'


class KauflandReceiptsContent(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = KauflandUserInterface()
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        layout = self.ui.init_ui()
        self.setLayout(layout)

    def connect_signals(self):
        self.ui.buttons.upload_button.clicked.connect(self.ui.upload_file)
        self.ui.buttons.submit_button.clicked.connect(self.ui.submit_receipt)
