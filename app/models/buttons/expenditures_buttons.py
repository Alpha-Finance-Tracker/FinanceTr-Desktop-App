from PySide6.QtWidgets import QWidget, QPushButton


class ExpendituresButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.Monthly = QPushButton("Monthly")
        self.Weekly = QPushButton("Weekly")
        self.Quarter = QPushButton("Quarter")
        self.Year = QPushButton('Year')
