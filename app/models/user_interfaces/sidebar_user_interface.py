from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame

from app.models.buttons.sidebar_buttons import SiderBarButtons


class SidebarUserInterface(QWidget):
    STYLE_SHEET = "background-color: #f0f0f0; border: none"
    def __init__(self,content_area):
        self.content_area = content_area
        super().__init__()

        self.buttons = SiderBarButtons(self.content_area)
        self.layout = QVBoxLayout()
        self.sidebar_frame = QFrame()
        self.frame_layout = None

    def init_ui(self):
        self.sidebar_frame.setStyleSheet(self.STYLE_SHEET)
        self.frame_layout = QVBoxLayout(self.sidebar_frame)

        for icon_path, action_key in self.buttons.BUTTONS:
            button = self.buttons.create_button(icon_path,action_key)
            self.frame_layout.addWidget(button)

        self.layout.addWidget(self.sidebar_frame)

        return self.layout
