from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

class Footer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Footer")
        self.label.setStyleSheet("background-color: lightblue; font-size: 16px; padding: 10px;")
        layout.addWidget(self.label)
        self.setLayout(layout)
