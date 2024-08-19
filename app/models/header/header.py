from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

class Header(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setStyleSheet("background-color: lightgreen; font-size: 18px; padding: 10px;")
        layout.addWidget(self.label)
        self.setLayout(layout)
