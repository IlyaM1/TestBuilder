from PyQt5.QtWidgets import QLabel, QMenu, QAction, QWidget, QHBoxLayout, QPushButton, QApplication
from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from Custom_Widgets.Clickable_label import Clickable_label
from config import Config


class Clickable_label_with_delete_buttons(QLabel):
    """
    QLabel на который можно нажать, который хранит в себе dictionary объекта для которого создан, также имеет контекстное меню из трёх действий: посмотреть детальную информацию(?), изменить, удалить
    """

    def __init__(self, text, dictionary, icon_see_path=Config().config["path"] + "\\Interface\\see_icon.png",
                 icon_edit_path=Config().config["path"] + "\\Interface\\edit_icon.png",
                 icon_delete_path=Config().config["path"] + "\\Interface\\Trash_Bin.png"):
        super().__init__()
        self.text = text
        self.dictionary = dictionary
        self.icon_see_path = icon_see_path
        self.icon_edit_path = icon_edit_path
        self.icon_delete_path = icon_delete_path
        self.init_UI()

    def init_UI(self):
        self.main_horizontal_layout = QHBoxLayout()

        self.label = Clickable_label(self.text, self.dictionary)
        self.main_horizontal_layout.addWidget(self.label)

        self.widget_for_layout_for_buttons = QWidget()
        self.layout_for_buttons = QHBoxLayout()

        see_icon = QIcon(self.icon_see_path)
        self.see_button = self.generate_image_button(see_icon, self.see_button_pressed)
        self.layout_for_buttons.addWidget(self.see_button)

        edit_icon = QIcon(self.icon_edit_path)
        self.edit_button = self.generate_image_button(edit_icon, self.edit_button_pressed)
        self.layout_for_buttons.addWidget(self.edit_button)

        delete_icon = QIcon(self.icon_delete_path)
        self.delete_button = self.generate_image_button(delete_icon, self.delete_button_pressed)
        self.layout_for_buttons.addWidget(self.delete_button)

        self.widget_for_layout_for_buttons.setLayout(self.layout_for_buttons)
        self.widget_for_layout_for_buttons.setMaximumWidth(150)
        # self.main_horizontal_layout.insertSpacing(1, 50)
        self.main_horizontal_layout.addWidget(self.widget_for_layout_for_buttons)

        self.setLayout(self.main_horizontal_layout)

    @staticmethod
    def generate_image_button(icon, press_function):
        button = QPushButton(icon=icon, text="")
        button.setStyleSheet("QPushButton{border:none;background-color:rgba(255, 255, 255,0);}")
        button.clicked.connect(press_function)
        return button

    def see_button_pressed(self):
        return

    def edit_button_pressed(self):
        return

    def delete_button_pressed(self):
        return


if __name__ == '__main__':
    app = QApplication([])
    auth_obj = Clickable_label_with_delete_buttons("123", "12")
    auth_obj.show()
    app.exec_()
