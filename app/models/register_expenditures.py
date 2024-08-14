import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMainWindow, QLabel
from PySide6.QtGui import QPainter, QBrush, QColor, QIcon
from PySide6.QtCore import Qt, QPoint, QSize
import math

class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        self.setStyleSheet("background-color: white;")
        self.icons = []
        self.buttons = []

    def add_icon(self, icon_path, position):
        button = QPushButton()
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(40, 40))
        button.setFixedSize(60, 60)
        button.setStyleSheet("background-color: transparent; border: none;")
        button.setToolTip(f"Expense {position}")  # ToolTip for demonstration
        self.buttons.append(button)
        self.icons.append(position)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.green))
        painter.setPen(Qt.NoPen)
        center = QPoint(self.width() // 2, self.height() // 2)
        radius = min(self.width(), self.height()) // 4
        painter.drawEllipse(center, radius, radius)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.arrange_icons()

    def arrange_icons(self):
        radius = min(self.width(), self.height()) // 4
        center = QPoint(self.width() // 2, self.height() // 2)
        angle_step = 360 / len(self.buttons) if self.buttons else 1
        for i, button in enumerate(self.buttons):
            angle = angle_step * i
            # Convert angle to radians
            angle_rad = math.radians(angle)
            x = center.x() + int(radius * 1.5 * math.cos(angle_rad))
            y = center.y() - int(radius * 1.5 * math.sin(angle_rad))
            button.move(x - button.width() // 2, y - button.height() // 2)

class ExpenditureDetail(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel(title, self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)