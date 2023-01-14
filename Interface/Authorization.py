from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QGroupBox, QHBoxLayout
from Interface.View_all_tests import View_all_tests
from Interface.Admin_view_tests_and_users import Admin_view_tests_and_users
from test_data_funcs import get_all_tests, get_users
from auth_reg import Signing
from db.sqlite import SQLInteract
from config import Config
from PyQt5 import QtCore, QtGui
import json


class Authorization(QWidget):
    """
    Окошко авторизации
    """

    def __init__(self):
        super().__init__()
        self.user = False
        self.cfg = Config()
        self.init_UI()

    def init_UI(self):
        self.set_window_settings()
        self.set_css()

        self.groupbox = self.generate_groupbox()

        vertical_layout = QVBoxLayout()

        self.input_label_login = self.generate_input_label("Фамилия", "input_label_login")
        vertical_layout.addWidget(self.input_label_login)

        self.input_label_password = self.generate_input_label("Пароль", "input_label_password")
        vertical_layout.addWidget(self.input_label_password)

        self.button_login = self.generate_login_button("Войти", self.button_login_pushed)
        vertical_layout.addWidget(self.button_login)

        vertical_layout.setAlignment(self.button_login, QtCore.Qt.AlignHCenter)
        self.groupbox.setLayout(vertical_layout)
        self.show()

    def set_window_settings(self):
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Авторизация")
        self.setWindowIcon(QtGui.QIcon(self.cfg.config["path"] + "/Interface/authorization.png"))

    def set_css(self):
        with open(self.cfg.config["path"] + '/Interface/css/Authorization.css') as f:
            self.setStyleSheet(f.read())

    @staticmethod
    def generate_input_label(placeholder_text, object_name):
        input_label_login = QLineEdit()
        input_label_login.setPlaceholderText(placeholder_text)
        input_label_login.setObjectName(object_name)
        input_label_login.setMaximumWidth(1000)

        return input_label_login

    @staticmethod
    def generate_login_button(text, connect_function):
        button_login = QPushButton(text)
        button_login.clicked.connect(connect_function)
        button_login.setMinimumWidth(300)
        button_login.move(QtCore.QPoint(230, 230))

        return button_login

    def generate_groupbox(self):
        groupbox = QGroupBox("", parent=self)
        groupbox.setFlat(True)
        groupbox.resize(400, 300)

        return groupbox

    # def resizeEvent(self, e):
    #     # if self.width() >= 1000:
    #     #     self.input_label_login.setMaximumWidth(1000)
    #     # else:
    #     #     self.input_label_login.setMaximumWidth()
    #     #     self.input_label_password.setStyleSheet("QLineEdit { width: 60% }")
    #     self.groupbox.move(QtCore.QPoint((self.width() - 400) / 2, (self.height() - 300) / 2))
    #     self.button_login.move(
    #         QtCore.QPoint((self.groupbox.width() - self.button_login.width()) / 2, self.button_login.y()))

    def button_login_pushed(self):
        auth_info = {"name": self.input_label_login.text().strip(),
                     "password": self.input_label_password.text().strip()}

        if auth_info["name"] == '' or auth_info["password"] == '':
            self.call_error_window("Вы ничего не ввели")
            return

        if auth_info["name"] == self.cfg.config["name"] and auth_info["password"] == self.cfg.config["password"]:
            self.next_window_for_admin()
        else:
            self.user = self.authorization(auth_info)
            if self.user is not False and self.user is not None:
                self.next_window_view_all_tests()
            else:
                self.call_error_window("Неправильный пароль или имя пользователя")

    def authorization(self, auth_info):
        s = SQLInteract(table_name='testcase', filename_db=self.cfg.config["path"] + '/db/users.db')
        sign_obj = Signing(auth_info, s)
        return sign_obj.authentication()

    def next_window_view_all_tests(self):
        test_db = SQLInteract(table_name='tests', filename_db=self.cfg.config["path"] + '/db/users.db',
                              values_of_this_table="(id, name, theme, max_result, questions)")
        test_arr = test_db.return_full_table(to_dict=True, element_for_transform="questions")
        self.close()
        self.view_all_tests = View_all_tests(tests=test_arr, user=self.user)

    def next_window_for_admin(self):
        user_db = SQLInteract(table_name='testcase', filename_db=self.cfg.config["path"] + '/db/users.db')
        test_db = SQLInteract(table_name='tests', filename_db=self.cfg.config["path"] + '/db/users.db',
                              values_of_this_table="(id, name, theme, max_result, questions)")
        user_arr = user_db.return_full_table(to_dict=True, element_for_transform="tests")
        test_arr = test_db.return_full_table(to_dict=True, element_for_transform="questions")
        self.close()
        self.admin_window = Admin_view_tests_and_users(tests=test_arr, users=user_arr)

    @staticmethod
    def call_error_window(text):
        error_window = QMessageBox()
        error_window.setText(text)
        error_window.setWindowTitle("Ошибка")
        error_window.exec()
