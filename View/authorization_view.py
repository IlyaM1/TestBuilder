from config import Config
from View.view import View
from Model.authorization_model import AuthInfo
from PyQt5 import QtWidgets, QtGui, QtCore
from View.ui_utils import UiUtils


class AuthorizationSignals(QtCore.QObject):
    login_clicked = QtCore.pyqtSignal()


class AuthorizationView(View):
    def __init__(self):
        super().__init__(AuthorizationSignals())

        self.__set_window_settings()
        self.__set_css()

        self.input_label_login = UiUtils.generate_input_label("Фамилия", "input_label_login")
        self.input_label_password = UiUtils.generate_input_label("Пароль", "input_label_password")
        self.button_login = UiUtils.generate_button("Войти", self.__button_login_pushed, QtCore.QPoint(230, 230))

        vertical_layout = UiUtils.generate_vertical_layout(self.input_label_login,
                                                           self.input_label_password,
                                                           self.button_login)
        vertical_layout.setAlignment(self.button_login, QtCore.Qt.AlignHCenter)

        self.groupbox = self.__generate_groupbox()
        self.groupbox.setLayout(vertical_layout)

    def get_auth_info(self):
        name = self.input_label_login.text()
        password = self.input_label_password.text()
        return AuthInfo(name, password)

    def __button_login_pushed(self):
        self.signals.login_clicked.emit()

    def __set_window_settings(self):
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Авторизация")
        self.setWindowIcon(QtGui.QIcon(Config.get_path() + "/View/img/authorization.png"))

    def __set_css(self):
        with open(Config.get_path() + '/View/css/authorization_view.css') as f:
            self.setStyleSheet(f.read())

    def __generate_groupbox(self):
        groupbox = QtWidgets.QGroupBox("", parent=self)
        groupbox.setFlat(True)
        groupbox.resize(400, 300)

        return groupbox


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    auth = AuthorizationView()
    auth.show()
    app.exec()
