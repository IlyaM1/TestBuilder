from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QPushButton, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from Custom_Widgets.Clickable_label import Clickable_label
from Interface.Admin_user_view import Admin_user_view
from Interface.Admin_test_view import Admin_test_view
from db.sqlite import SQLInteract
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
        self.type = self.check_dict_type()
        self.answer_of_deleting = ""
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
        self.main_horizontal_layout.addWidget(self.widget_for_layout_for_buttons)

        self.setLayout(self.main_horizontal_layout)

    @staticmethod
    def generate_image_button(icon, press_function):
        button = QPushButton(icon=icon, text="")
        button.setStyleSheet("QPushButton{border:none;background-color:rgba(255, 255, 255,0);}")
        button.clicked.connect(press_function)
        return button

    def check_dict_type(self):
        if "post" in self.dictionary:
            return "user"
        else:
            return "test"

    def see_button_pressed(self):
        return

    def edit_button_pressed(self):
        if self.type == "test":
            self.opened_widget = Admin_test_view(self.dictionary)
        elif self.type == "user":
            self.opened_widget = Admin_user_view(self.dictionary)
        return

    def delete_button_pressed(self):
        if self.type == "test":
            self.call_sure_delete_window()
            if self.answer_of_deleting == "OK":
                print("deleted")
                # TODO: make deleting of test from BD
            else:
                print("NOT deleted")
        elif self.type == "user":
            self.call_sure_delete_window()
            if self.answer_of_deleting == "OK":
                user_bd = SQLInteract(table_name='testcase', filename_db=Config().config["path"] + '/db/users.db')
                # SQLInteract.sql_delete_one(id=self.dictionary["id"])
                # TODO: make deleting of test from BD
                print("deleted")
            else:
                print("NOT deleted")
        return

    def call_sure_delete_window(self):
        question_window = QMessageBox()
        question_window.setWindowTitle("Проверка")
        question_window.setText("Вы уверены, что хотите удалить?")
        question_window.setIcon(QMessageBox.Question)
        question_window.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        question_window.buttonClicked.connect(self.answer_sure_delete_window)

        question_window.show()
        question_window.exec_()

    def answer_sure_delete_window(self, message):
        if message.text() == "OK":
            self.answer_of_deleting = "OK"
        else:
            self.answer_of_deleting = "Cancel"


if __name__ == '__main__':
    app = QApplication([])
    auth_obj = Clickable_label_with_delete_buttons("123", "12")
    auth_obj.show()
    app.exec_()
