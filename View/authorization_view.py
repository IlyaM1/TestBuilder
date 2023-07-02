from config import Config
from View.view import View
from Model.authorization_model import AuthInfo
from PyQt5 import QtWidgets, QtGui, QtCore


class AuthorizationSignals(QtCore.QObject):
    login_clicked = QtCore.pyqtSignal()


class AuthorizationView(View):
    def __init__(self):
        super().__init__(AuthorizationSignals())

        self.set_window_settings()
        self.set_css()

        self.input_label_login = self.generate_input_label("Фамилия", "input_label_login")
        self.input_label_password = self.generate_input_label("Пароль", "input_label_password")
        self.button_login = self.generate_login_button("Войти", self.button_login_pushed)

        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.addWidget(self.input_label_login)
        vertical_layout.addWidget(self.input_label_password)
        vertical_layout.addWidget(self.button_login)
        vertical_layout.setAlignment(self.button_login, QtCore.Qt.AlignHCenter)

        self.groupbox = self.generate_groupbox()
        self.groupbox.setLayout(vertical_layout)

    def button_login_pushed(self):
        self.signals.login_clicked.emit()

    def get_auth_info(self):
        name = self.input_label_login.text()
        password = self.input_label_password.text()
        return AuthInfo(name, password)

    def set_window_settings(self):
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Авторизация")
        self.setWindowIcon(QtGui.QIcon(Config.get_path() + "/View/img/authorization.png"))

    def set_css(self):
        with open(Config.get_path() + '/View/css/authorization_view.css') as f:
            self.setStyleSheet(f.read())

    @staticmethod
    def generate_input_label(placeholder_text, object_name=None):
        input_label_login = QtWidgets.QLineEdit()
        input_label_login.setPlaceholderText(placeholder_text)
        input_label_login.setObjectName(object_name)
        input_label_login.setMaximumWidth(1000)

        return input_label_login

    @staticmethod
    def generate_login_button(text, connect_function):
        button_login = QtWidgets.QPushButton(text)
        button_login.clicked.connect(connect_function)
        button_login.setMinimumWidth(300)
        button_login.move(QtCore.QPoint(230, 230))

        return button_login

    def generate_groupbox(self):
        groupbox = QtWidgets.QGroupBox("", parent=self)
        groupbox.setFlat(True)
        groupbox.resize(400, 300)

        return groupbox

    @staticmethod
    def call_error_window(text):
        error_window = QtWidgets.QMessageBox()
        error_window.setText(text)
        error_window.setWindowTitle("Ошибка")
        error_window.exec()
