import os
import requests
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QCalendarWidget
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt, QDate, QCoreApplication
from dotenv import load_dotenv

from app.utils.auth_service import prepare_token_for_request

load_dotenv()
finance_service = 'http://127.0.0.1:8001'


class KauflandReceiptsContent(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.layout = QVBoxLayout(self)
        self.label = QLabel("No file selected", self)
        self.date_input = QCalendarWidget()
        self.upload_button = QPushButton("Upload Receipt", self)
        self.submit_button = QPushButton("Submit", self)
        self.loading_label = QLabel(self)
        self.loading_movie = QMovie("images/gree-loader.gif")
        self.file_name = None

    def init_ui(self):

        self.date_input.setGridVisible(True)
        self.date_input.setSelectedDate(QDate.currentDate())
        self.loading_label.setMovie(self.loading_movie)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.hide()  # Initially hide the loading icon

        self.layout.addWidget(self.upload_button)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.loading_label)  # Add loading label to layout

        self.upload_button.clicked.connect(self.upload_file)
        self.submit_button.clicked.connect(self.on_submit_clicked)

    def upload_file(self):

        file_name, _ = QFileDialog.getOpenFileName(self, "Select File")

        if file_name:
            self.file_name = file_name
            self.label.setText(file_name)
            print(f"File selected: {file_name}")
        else:
            self.file_name = None
            self.label.setText("No file selected")

    def on_submit_clicked(self):
        if not self.file_name:
            self.label.setText("No file to upload")
            return

        token = prepare_token_for_request()
        update_url = f"{finance_service}/Finance_tracker/kaufland_receipt"
        headers = {'Authorization': f'Bearer {token}'}

        self.date_input.hide()
        self.loading_label.show()
        self.loading_movie.start()

        QCoreApplication.processEvents()

        try:
            with open(self.file_name, 'rb') as file:
                files = {'image': (os.path.basename(self.file_name), file)}
                data = {
                    'date': self.date_input.selectedDate().toString('dd.MM.yyyy')
                }
                response = requests.post(update_url, headers=headers, files=files, params=data)
                response.raise_for_status()
                self.label.setText(f"Upload successful: {response.status_code}")
        except requests.RequestException as e:
            self.label.setText(f"Upload failed: {e}")
        finally:
            self.date_input.show()
            self.loading_movie.stop()
            self.loading_label.hide()
