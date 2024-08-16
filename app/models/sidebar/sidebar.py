
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
        self.sidebar_frame.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
        frame_layout = QVBoxLayout(self.sidebar_frame)

        buttons = [
            ("Expenditures", self.expenditures_on_click),
            ("K-receipts", None),
            ("FinanceTr", self.financeTR_on_click),
            ("Profile", None),
            ("Logout", None),
        ]

        for name, handler in buttons:
            button = QPushButton(name)
            button.clicked.connect(handler)
            frame_layout.addWidget(button)

        layout.addWidget(self.sidebar_frame)
        self.setLayout(layout)

    def expenditures_on_click(self,token):
        self.content_area.show_expenditures(self._token)

    def financeTR_on_click(self):
        self.content_area.show_financeTR(self._token)
