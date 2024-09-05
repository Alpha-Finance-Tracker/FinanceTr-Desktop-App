from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame

class Sidebar(QWidget):
    ICON_SIZE = QSize(32, 32)
    STYLE_SHEET = "background-color: #f0f0f0; border: none"
    BUTTONS = [
        ('images/sidebar/home.png', 'home'),
        ('images/sidebar/analytics.PNG', 'expenditures'),
        ('images/sidebar/financeTr.png', 'finance'),
        ('images/sidebar/kaufland_logo.png', 'kaufland'),
        ('images/sidebar/lidl_logo.png', 'lidl'),
        ('images/sidebar/stock.jpg', 'stock')
    ]

    def __init__(self, content_area):
        super().__init__()
        self.content_area = content_area
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        sidebar_frame = QFrame()
        sidebar_frame.setStyleSheet(self.STYLE_SHEET)
        frame_layout = QVBoxLayout(sidebar_frame)

        for icon_path, action_key in self.BUTTONS:
            button = self.create_button(icon_path, action_key)
            frame_layout.addWidget(button)

        layout.addWidget(sidebar_frame)
        self.setLayout(layout)

    def create_button(self, icon_path, action_key):
        button = QPushButton()
        button.setIcon(QIcon(icon_path))
        button.setIconSize(self.ICON_SIZE)
        button.clicked.connect(lambda: self.handle_click(action_key))
        return button

    def handle_click(self, action_key):
        actions = {
            'home': self.content_area.show_home,
            'expenditures': self.content_area.show_expenditures,
            'finance': self.content_area.show_financeTR,
            'kaufland': self.content_area.show_receipt_menu,
            'lidl': self.content_area.show_receipt_menu,
        }
        action = actions.get(action_key)
        if action:
            action()
