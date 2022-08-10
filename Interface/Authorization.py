from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from Interface.View_all_tests import View_all_tests
from test_data_funcs import get_all_tests, get_users
from auth_reg import Signing


class Authorization(QWidget):

    def __init__(self):
        super().__init__()
        self.user_login_password = ()
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(400, 300)
        vertical_layout = QVBoxLayout()

        with open('Interface/css/Authorization.css') as f:
            self.setStyleSheet(f.read())

        self.input_label_login = QLineEdit()
        self.input_label_login.setPlaceholderText("Фамилия")
        self.input_label_login.setObjectName("input_label_login")
        vertical_layout.addWidget(self.input_label_login)

        self.input_label_password = QLineEdit()
        self.input_label_password.setPlaceholderText("Пароль")
        vertical_layout.addWidget(self.input_label_password)

        button_login = QPushButton("Войти")
        button_login.clicked.connect(self.button_login_pushed)
        vertical_layout.addWidget(button_login)

        self.setLayout(vertical_layout)
        self.show()

    def button_login_pushed(self):
        self.user_login_password = (self.input_label_login.text(), self.input_label_password.text())
        # user = get_user(self.user_login_password)
        user = {"id": 0, "name": self.user_login_password[0], "password": self.user_login_password[1], "post": "",
                "tests": '[]'}
        if user is not None:
            self.close()
            test = get_all_tests(user)[0]
            tests = [test for i in range(20)]
            self.view_all_tests = View_all_tests(tests, user)

    def authorization(self):
        pass
