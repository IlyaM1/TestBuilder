from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QApplication, QSizePolicy, \
    QListWidget, QMainWindow, QScrollArea
from PyQt5.QtCore import QSize, Qt
from Interface.Solving_test_widget import Solving_test_widget
from Custom_Widgets.Clickable_label import Clickable_label
from test_data_funcs import get_all_tests, get_users
from config import Config


class View_all_tests(QMainWindow):
    """
    Просмотр списка всех тестов за юзера
    """

    def __init__(self, tests, user):
        super().__init__()
        self.tests = tests
        self.user = user
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)
        self.scroll_widget = QScrollArea()
        self.central_widget = QWidget()

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addSpacing(10)

        with open(Config().config["path"] + '\\Interface\\css\\View_all_tests.css') as css:
            self.setStyleSheet(css.read())

        for test in self.tests:
            test_row = Clickable_label(f'{test["name"]}: {len(test["questions"])} вопроса', test)
            test_row.setFixedSize(self.width() - 40, 120)
            test_row.clicked.connect(lambda: self.label_test_pushed(test_row))
            self.vertical_layout.addWidget(test_row)

        self.central_widget.setLayout(self.vertical_layout)

        self.scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_widget.setWidgetResizable(True)
        self.scroll_widget.setWidget(self.central_widget)

        self.setCentralWidget(self.scroll_widget)

        self.setGeometry(600, 100, 1000, 900)

        self.show()

    def label_test_pushed(self, pushed_label):
        self.close()
        self.solve = Solving_test_widget(test=pushed_label.dictionary, user=self.user)
        # print(pushed_label.dictionary)


if __name__ == "__main__":
    app = QApplication([])
    user = get_users()[0]
    test = get_all_tests(user)[0]
    tests = [test for i in range(2)]
    view_all_tests = View_all_tests(tests, user)

    app.exec_()
