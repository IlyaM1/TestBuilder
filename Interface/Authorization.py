from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from Interface.View_all_tests import View_all_tests
from test_data_funcs import get_all_tests, get_users

class Authorization(QWidget):

    def __init__(self):
        super().__init__()
        self.user_login_password = ()
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(400, 300)
        vertical_layout = QVBoxLayout()

        with open('Interface/Authorization.css') as f:
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
        user = {"name": "Vlad"}
        if user is not None:
            self.close()
            tests = get_all_tests(user)
            self.view_all_tests = View_all_tests(tests, user)
