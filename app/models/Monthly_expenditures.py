import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QGraphicsView, QGraphicsScene, QGraphicsRectItem
)
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import Qt

class MonthlyExpenditures(QWidget):
    def __init__(self, data ):
        super().__init__()
        self.setWindowTitle("Monthly Expenditures")
        self.resize(800, 600)

        # Data for plotting
        self.months = list(data.keys())
        self.expenditures = list(data.values())

        # Set up the layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create the graphics view and scene
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.layout.addWidget(self.view)

