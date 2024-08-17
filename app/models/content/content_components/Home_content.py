from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        welcome_label = QLabel("Welcome to the Home Page!")
        layout.addWidget(welcome_label)
        self.setLayout(layout)