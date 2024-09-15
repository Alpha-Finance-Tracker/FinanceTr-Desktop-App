from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton


class FinanceTrackerButtons(QWidget):

    def __init__(self,type_layout):
        self.type_layout = type_layout
        self.category_buttons = {}
        self.type_buttons = {}
        self.selected_type = None
        self.selected_category = None

        super().__init__()


    def add_category_button(self, name, image_path):
        button = QPushButton(self)
        button.setIcon(QIcon(image_path))
        button.setIconSize(QSize(64, 64))
        button.setCheckable(True)
        button.clicked.connect(lambda: self.select_category(name))
        self.category_buttons[name] = button

    def add_type_button(self, name, image_path, categories):
        button = QPushButton(self)
        button.setIcon(QIcon(image_path))
        button.setIconSize(QSize(64, 64))
        button.setCheckable(True)
        button.clicked.connect(lambda: self.select_type(name))
        button.hide()
        self.type_buttons[name] = {'button': button, 'categories': categories}


    def select_type(self, type_name):
        for btn_name, button_info in self.type_buttons.items():
            button_info['button'].setChecked(btn_name == type_name)
        self.selected_type = type_name

    def select_category(self, category_name):
        for btn_name, button in self.category_buttons.items():
            button.setChecked(btn_name == category_name)
        self.selected_category = category_name

        for i in reversed(range(self.type_layout.count())):
            widget = self.type_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)


        for button_info in self.type_buttons.values():
            if category_name in button_info['categories']:
                button_info['button'].show()
                self.type_layout.addWidget(button_info['button'])
            else:
                button_info['button'].hide()


    def set_category_buttons(self):
        self.add_category_button('Food', 'images/categories/food.png')
        self.add_category_button('Transport', 'images/categories/transportation.png')
        self.add_category_button('Health', 'images/categories/health.png')
        self.add_category_button('Entertainment', 'images/categories/entertainment.png')
        self.add_category_button('Home', 'images/categories/home.jpg')
        self.add_category_button('Sport', 'images/categories/sport.png')

    def set_type_buttons(self):
        self.add_type_button('Animal', 'images/types/food/animal.jpg', categories=['Food'])
        self.add_type_button('Dairy', 'images/types/food/dairy.png', categories=['Food'])
        self.add_type_button('Nuts', 'images/types/food/nuts.png', categories=['Food'])
        self.add_type_button('Vegetables', 'images/types/food/vegetables.png', categories=['Food'])
        self.add_type_button('Beverages', 'images/types/food/beverages.png', categories=['Food'])

        self.add_type_button('Communications', 'images/types/home/communications.jpg', categories=['Home'])
        self.add_type_button('Electricity', 'images/types/home/electricity.png', categories=['Home'])
        self.add_type_button('Water', 'images/types/home/water.png', categories=['Home'])


        self.add_type_button('Transport', 'images/categories/transportation.png', categories=['Transport'])

        self.add_type_button('Health', 'images/categories/health.png', categories=['Health'])

        self.add_type_button('Entertainment', 'images/categories/entertainment.png', categories=['Entertainment'])

        self.add_type_button('Sport', 'images/categories/sport.png', categories=['Sport'])





