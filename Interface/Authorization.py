from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class Authorization(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.vertical_layout = QVBoxLayout()

        input_label_login = QLineEdit()
        input_label_login.setPlaceholderText("Фамилия")
        self.vertical_layout.addWidget(input_label_login)

        input_label_password = QLineEdit()
        input_label_password.setPlaceholderText("Пароль")
        self.vertical_layout.addWidget(input_label_password)

        button_login = QPushButton("Войти")
        button_login.clicked.connect(self.button_login_pushed)
        self.vertical_layout.addWidget(button_login)


        self.setLayout(self.vertical_layout)
        self.show()

    def button_login_pushed(self):
        pass