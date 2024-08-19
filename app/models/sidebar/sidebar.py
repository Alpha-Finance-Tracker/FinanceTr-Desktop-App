from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import  QWidget, QVBoxLayout, QPushButton, QFrame
class Sidebar(QWidget):
    def __init__(self, content_area, token):
        super().__init__()
        self.content_area = content_area
        self._token = token
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.sidebar_frame = QFrame()
        self.sidebar_frame.setStyleSheet("background-color: #f0f0f0; border: none")
        frame_layout = QVBoxLayout(self.sidebar_frame)

        buttons = [
            ('images/sidebar/home.png',self.home_on_click),
            ("images/sidebar/analytics.PNG", self.expenditures_on_click),
            ("images/sidebar/financeTr.png", self.financeTR_on_click),
            ("images/sidebar/receipts.png", self.shopping_receipts_on_click),
            # ("Logout", None),
        ]

        for icon_path, handler in buttons:
            button = QPushButton()
            button.setIcon(QIcon(icon_path))
            button.setIconSize(QSize(32, 32))  # Adjust size as needed
            button.clicked.connect(handler)
            frame_layout.addWidget(button)

        layout.addWidget(self.sidebar_frame)
        self.setLayout(layout)

    def home_on_click(self):
        self.content_area.show_home()

    def expenditures_on_click(self):
        self.content_area.show_expenditures()

    def financeTR_on_click(self):
        self.content_area.show_financeTR()

    def shopping_receipts_on_click(self):
        self.content_area.show_receipt_menu()
