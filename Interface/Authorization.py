from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit

class Authorization(QWidget):

    def __init__(self):
        super().__init__()
        self.tup = ()
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(400, 300)
        vertical_layout = QVBoxLayout()

        with open('Interface/Authorization.css') as f:
            self.setStyleSheet(f.read())

        self.input_label_login = QLineEdit()
        self.input_label_login.setPlaceholderText("Фамилия")
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
        self.tup = (self.input_label_login.text(), self.input_label_password.text())
        print(self.tup)
        self.close()