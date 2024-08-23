from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.background_label = QLabel(self)
        self.pixmap = QPixmap("images/FinanceTr_wallpaper.PNG")
        self.update_background()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.resizeEvent = self.on_resize

    def on_resize(self, event):

        self.update_background()
        event.accept()

    def update_background(self):

        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)


        self.background_label.setPixmap(scaled_pixmap)


        self.background_label.setGeometry(
            (self.width() - scaled_pixmap.width()) // 2,
            (self.height() - scaled_pixmap.height()) // 2,
            scaled_pixmap.width(),
            scaled_pixmap.height()
        )
