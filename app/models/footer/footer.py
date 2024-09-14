from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

from app.models.user_interfaces.footer_user_interface import FooterUserInterface


class Footer(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = FooterUserInterface()
        self.init_ui()

    def init_ui(self):
        layout =  self.ui.init_ui()
        self.setLayout(layout)
