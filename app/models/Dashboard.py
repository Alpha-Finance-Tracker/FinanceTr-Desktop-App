import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget

from app.models.content import Content
from app.models.footer import Footer
from app.models.header import Header
from app.models.sidebar import Sidebar


class Dashboard(QMainWindow):
    def __init__(self,token):
        self._token = token
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.resize(1000, 800)


        # Central widget and grid layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.central_widget.setLayout(self.grid_layout)

        # Create and add sections
        self.header = Header()
        self.content = Content()
        self.sidebar = Sidebar(self.content,self._token)
        self.footer = Footer()

        # Add widgets to grid layout
        self.grid_layout.addWidget(self.header, 0, 0, 1, 2)  # Header spans 2 columns
        self.grid_layout.addWidget(self.sidebar, 1, 0)  # Sidebar in first column
        self.grid_layout.addWidget(self.content, 1, 1)  # Content in second column
        self.grid_layout.addWidget(self.footer, 2, 0, 1, 2)  # Footer spans 2 columns

        # Adjust row and column stretch factors
        self.grid_layout.setRowStretch(1, 1)  # Make the main content area expand
        self.grid_layout.setColumnStretch(1, 2)  # Make the content column expand more than the sidebar

    @property
    def token(self):
        return self._token