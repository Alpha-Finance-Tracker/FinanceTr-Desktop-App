from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QPushButton, QFrame


class Sidebar(QWidget):
    def __init__(self, content_area):
        super().__init__()
        self.content_area = content_area
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a frame to hold the buttons
        self.sidebar_frame = QFrame()
        self.sidebar_frame.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc;")
        frame_layout = QVBoxLayout(self.sidebar_frame)

        # Add 5 unique buttons to the frame
        buttons = [
            ("Dashboard", self.show_dashboard),
            ("K-receipts", self.show_reports),
            ("FinanceTr", self.show_settings),
            ("Profile", self.show_profile),
            ("Logout", self.show_logout),
        ]

        for name, handler in buttons:
            button = QPushButton(name)
            button.clicked.connect(handler)
            frame_layout.addWidget(button)

        layout.addWidget(self.sidebar_frame)
        self.setLayout(layout)

    def show_dashboard(self):
        self.content_area.setCurrentIndex(0)

    def show_reports(self):
        self.content_area.setCurrentIndex(1)

    def show_settings(self):
        self.content_area.setCurrentIndex(2)

    def show_profile(self):
        self.content_area.setCurrentIndex(3)

    def show_logout(self):
        self.content_area.setCurrentIndex(4)
