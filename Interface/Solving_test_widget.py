from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtCore import QSize, Qt
from test_data_funcs import get_all_tests

class Solving_test_widget(QWidget):

    def __init__(self, test = {}, parent=None):
        super(QWidget, self).__init__(parent)
        self.test = test
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        with open('css/Solving_test_widget.css') as css:
            self.setStyleSheet(css.read())

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    test = get_all_tests()[0]
    solve_test = Solving_test_widget(test=test)

    app.exec_()