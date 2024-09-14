from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame

from app.models.user_interfaces.sidebar_user_interface import SidebarUserInterface


class Sidebar(QWidget):
    def __init__(self, content_area):
        super().__init__()
        self.content_area = content_area
        self.ui = SidebarUserInterface(self.content_area)
        self.init_ui()

    def init_ui(self):
        layout = self.ui.init_ui()
        self.setLayout(layout)