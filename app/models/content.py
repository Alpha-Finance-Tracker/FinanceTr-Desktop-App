from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QStackedWidget


class Content(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Add different content widgets
        contents = [
            "Dashboard Content",
            "Reports Content",
            "Settings Content",
            "Profile Content",
            "Logout Content"
        ]

        for content in contents:
            label = QLabel(content)
            label.setStyleSheet("font-size: 24px; padding: 20px;")
            label.setAlignment(Qt.AlignCenter)
            self.addWidget(label)