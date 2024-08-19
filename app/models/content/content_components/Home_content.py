from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create a label for the image
        self.background_label = QLabel(self)

        # Load the image
        self.pixmap = QPixmap("images/FinanceTr_wallpaper.PNG")

        # Scale the image to fit within the window, maintaining aspect ratio
        self.update_background()

        # Create a layout and add widgets
        layout = QVBoxLayout()

        # Set the layout for the QWidget
        self.setLayout(layout)

        # Update the size and position of the image background when the window is resized
        self.resizeEvent = self.on_resize

    def on_resize(self, event):
        # Update the background whenever the window is resized
        self.update_background()
        event.accept()

    def update_background(self):
        # Scale the image while maintaining aspect ratio
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set the pixmap to the label
        self.background_label.setPixmap(scaled_pixmap)

        # Center the image within the window
        self.background_label.setGeometry(
            (self.width() - scaled_pixmap.width()) // 2,
            (self.height() - scaled_pixmap.height()) // 2,
            scaled_pixmap.width(),
            scaled_pixmap.height()
        )
