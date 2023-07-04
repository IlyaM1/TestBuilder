import sys
from PyQt5 import QtWidgets

from window_manager import WindowManager


class Application(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.window_manager = WindowManager.get_instance()
        self.window_manager.auth_view.show()
        sys.exit(self.exec_())


def main():
    app = Application(sys.argv)


if __name__ == '__main__':
    main()
