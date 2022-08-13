from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QApplication, QSizePolicy, QListWidget, QMainWindow, QScrollArea
from PyQt5.QtCore import QSize, Qt
from Custom_Widgets.Item import Item
from test_data_funcs import get_all_tests, get_users
class View_all_tests(QMainWindow):

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

        with open('css/View_all_tests.css') as f:
            self.setStyleSheet(f.read())

        for test in self.tests:
            test_row = Item(f'{test["name"]}: {len(test["questions"])} вопроса', test["id"])
            test_row.setFixedSize(self.width()-40, 120)
            test_row.clicked.connect(self.label_test_pushed)
            self.vertical_layout.addWidget(test_row)

        self.central_widget.setLayout(self.vertical_layout)

        self.scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_widget.setWidgetResizable(True)
        self.scroll_widget.setWidget(self.central_widget)

        self.setCentralWidget(self.scroll_widget)

        self.setGeometry(600, 100, 1000, 900)

        self.show()

    def label_test_pushed(self):
        pass

    def button_login_pushed(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    user = get_users()[0]
    test = get_all_tests(user)[0]
    tests = [test for i in range(20)]
    view_all_tests = View_all_tests(tests, user)

    app.exec_()
