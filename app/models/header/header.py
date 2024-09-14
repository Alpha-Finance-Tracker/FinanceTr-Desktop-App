from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

from app.models.user_interfaces.header_user_interface import HeaderUserInterface


class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = HeaderUserInterface()
        self.init_ui()

    def init_ui(self):
        layout =  self.ui.init_ui()
        self.setLayout(layout)

