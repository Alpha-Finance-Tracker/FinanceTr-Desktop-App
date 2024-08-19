from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt


class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create a label for the GIF
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())  # Set label size to the window size

        # Load the GIF
        movie = QMovie("images/FinanceTr_wallpaper.PNG")
        self.background_label.setMovie(movie)
        movie.start()

        # Create a layout and add widgets
        layout = QVBoxLayout()

        # Set the layout for the QWidget
        self.setLayout(layout)

        # Raise the welcome label above the GIF background
        self.background_label.lower()  # Send the background label to the back

        # Update the size of the GIF background when the window is resized
        self.resizeEvent = self.on_resize

    def on_resize(self, event):
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        event.accept()

