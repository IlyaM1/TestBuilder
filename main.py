import sys
from PyQt5 import QtWidgets
from View.authorization_view import AuthorizationView
from Model.authorization_model import AuthorizationModel
from Presenter.authorization_presenter import AuthorizationPresenter


class Application(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        auth_view = AuthorizationView()
        auth_model = AuthorizationModel()
        auth_presenter = AuthorizationPresenter(auth_view, auth_model)

        auth_view.show()
        sys.exit(self.exec_())


def main():
    app = Application(sys.argv)


if __name__ == '__main__':
    main()
