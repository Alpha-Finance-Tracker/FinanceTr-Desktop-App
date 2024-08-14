import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(800, 600)

        # Central widget and grid layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)

        # Set up initial grid layout positions
        self.setup_grid()

    def setup_grid(self):
        """Setup initial grid layout with fixed sizes and size policies."""
        # Create widgets
        self.label1 = Q("Label 1")
        self.label2 = QLabel("Label 2")


        # Set sizes and policies
        self.label1.setFixedSize(100, 50)

        self.label2.setMinimumSize(80, 30)


        # Add widgets to grid layout
        self.grid_layout.addWidget(self.label1, 0, 0)  # Row 0, Column 0
        self.grid_layout.addWidget(self.label2, 4, 1)  # Row 0, Column 1



        # Set stretch factors
        self.grid_layout.setRowStretch(1, 1)
        self.grid_layout.setColumnStretch(0, 2)

    def add_component(self, widget, row, column):
        """Add a widget to a specific position in the grid."""
        self.layout.addWidget(widget, row, column)
