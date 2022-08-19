from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from Interface.View_all_tests import View_all_tests
from test_data_funcs import get_all_tests, get_users
from auth_reg import Signing
from db.sqlite import SQLInteract
from config import Config
from PyQt5 import QtCore
import json


class Authorization(QWidget):
    """
    Окошко авторизации
    """
    def __init__(self):
        super().__init__()
        self.user_login_password = ()
        self.user = False
        self.init_UI()
        self.cfg = Config()
        # print(self.cfg.config)

    def init_UI(self):
        self.setMinimumSize(400, 300)
        vertical_layout = QVBoxLayout()

        with open('Interface/css/Authorization.css') as f:
            self.setStyleSheet(f.read())

        self.input_label_login = QLineEdit()
        self.input_label_login.setPlaceholderText("Фамилия")
        self.input_label_login.setObjectName("input_label_login")
        self.input_label_login.setAlignment(QtCore.Qt.AlignBaseline)
        # self.input_label_login.textChanged.connect(self.on_text_changed)
        vertical_layout.addWidget(self.input_label_login)

        self.input_label_password = QLineEdit()
        self.input_label_password.setPlaceholderText("Пароль")
        # self.input_label_password.setAlignment(QtCore.Qt.AlignCenter)
        vertical_layout.addWidget(self.input_label_password)

        button_login = QPushButton("Войти")
        button_login.clicked.connect(self.button_login_pushed)
        vertical_layout.addWidget(button_login)

        self.setLayout(vertical_layout)
        self.show()

    def button_login_pushed(self):
        self.user_login_password = (self.input_label_login.text().strip(), self.input_label_password.text().strip())

        if self.user_login_password[0] == '' or self.user_login_password[1] == '':
            error_window = QMessageBox()
            error_window.setText("Вы ничего не ввели")
            error_window.setWindowTitle("Ошибка")
            error_window.exec()
            return

        if self.user_login_password[0] == self.cfg["name"] and self.user_login_password[1] == self.cfg["password"]:
            self.next_window_for_admin()  # TODO: next_window_for_admin func
        else:
            self.user = {"id": 0, "name": self.user_login_password[0], "password": self.user_login_password[1],
                         "post": "",
                         "tests": '[]'}
            self.user = self.authorization()
            if self.user is not False:
                self.next_window_view_all_tests()
            elif self.user is False:
                error_window = QMessageBox()
                error_window.setText("Неправильный пароль или имя пользователя")
                error_window.setWindowTitle("Ошибка")
                error_window.exec()

    def authorization(self):
        s = SQLInteract(table_name='testcase', filename_db=self.cfg.config["path"] + '/db/users.db')
        sign_obj = Signing(self.user, s)
        return sign_obj.authentication()

    def next_window_view_all_tests(self):
        if self.user is not None:
            self.close()
            test = get_all_tests(self.user)[0]
            tests = [test for i in range(20)]
            self.view_all_tests = View_all_tests(tests, self.user)

    def next_window_for_admin(self):
        print("You entered as admin") # to do
