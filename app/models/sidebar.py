from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Sidebar")
        self.label.setStyleSheet("background-color: lightgray; font-size: 16px; padding: 10px;")
        layout.addWidget(self.label)
        self.setLayout(layout)
