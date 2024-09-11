from PySide6.QtWidgets import QWidget, QPushButton


class KauflandButtons(QWidget):

    def __init__(self):
        super().__init__()
        self.upload_button = QPushButton("Upload Receipt", self)
        self.submit_button = QPushButton("Submit", self)