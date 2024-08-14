from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

class Content(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Content Area")
        self.label.setStyleSheet("background-color: purple; font-size: 14px; padding: 10px;")
        self.info_display = None
        # layout.addWidget(self.info_display)

        self.setLayout(layout)
