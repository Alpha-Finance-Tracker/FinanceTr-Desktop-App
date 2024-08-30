from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget
from app.models.content.content import Content
from app.models.footer.footer import Footer
from app.models.header.header import Header
from app.models.sidebar.sidebar import Sidebar

class Dashboard(QMainWindow):
    WINDOW_TITLE = "FinanceTr"
    WINDOW_ICON_PATH = 'images/app_icon.png'
    WINDOW_SIZE = (1000, 800)

    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_layout()
        self.initialize_widgets()
        self.configure_layout()
        self.start_home()

    def setup_window(self):
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowIcon(QIcon(self.WINDOW_ICON_PATH))
        self.resize(*self.WINDOW_SIZE)

    def setup_layout(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.central_widget.setLayout(self.grid_layout)

    def initialize_widgets(self):
        self.header = Header()
        self.content = Content()
        self.sidebar = Sidebar(self.content)
        self.footer = Footer()

    def configure_layout(self):
        self.grid_layout.addWidget(self.header, 0, 0, 1, 2)  # Header spans 2 columns
        self.grid_layout.addWidget(self.sidebar, 1, 0)  # Sidebar in first column
        self.grid_layout.addWidget(self.content, 1, 1)  # Content in second column
        self.grid_layout.addWidget(self.footer, 2, 0, 1, 2)  # Footer spans 2 columns
        self.grid_layout.setRowStretch(1, 1)
        self.grid_layout.setColumnStretch(1, 2)

    def start_home(self):
        self.content.show_home()
