from PySide6.QtCore import QDate, QCoreApplication
from PySide6.QtWidgets import QWidget, QCalendarWidget, QLabel, QFormLayout, QVBoxLayout, QFileDialog

from app.models.buttons.kaufland_buttons import KauflandButtons
from app.models.data_streams.kaufland_ds import KauflandDs
from app.utils.auth_service import prepare_token_for_request


class KauflandUserInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.date_input = QCalendarWidget()
        self.buttons = KauflandButtons()

        self.label = QLabel("No file selected", self)
        self.file_name = None

    def init_ui(self):
        self.date_input.setGridVisible(True)
        self.date_input.setSelectedDate(QDate.currentDate())
        self.layout.addWidget(self.buttons.upload_button)
        self.layout.addWidget(self.buttons.submit_button)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.label)
        return self.layout


    def upload_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File")

        if file_name:
            self.file_name = file_name
            self.label.setText(file_name)
            print(f"File selected: {file_name}")
        else:
            self.file_name = None
            self.label.setText("No file selected")

    def submit_receipt(self):
        token = prepare_token_for_request()
        self.date_input.hide()
        QCoreApplication.processEvents()

        data = {'file': self.file_name,
                'date': self.date_input.selectedDate().toString('dd.MM.yyyy')}

        service = KauflandDs(token)
        response = service.request(data)

        display = service.display(response)

        self.label.setText(display)





