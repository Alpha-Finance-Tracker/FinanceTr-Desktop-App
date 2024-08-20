from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt


class ReceiptsContent(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create a label for the GIF
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())  # Set label size to the window size
        self.button = QPushButton("Receipts")
        self.button.clicked.connect(self.on_button_clicked)



        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)


    def on_button_clicked(self):
        pass


    def on_resize(self, event):
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        event.accept()

