from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout
from Interface.Item import Item
from test_data_funcs import get_all_tests, get_users
from functools import partial
class Admin_view_tests_and_users(QWidget):

    def __init__(self, parent=None, tests = [], users = []):
        super(QWidget, self).__init__(parent)
        self.tests = tests
        self.users = users
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        self.container = QVBoxLayout(self)

        self.tab_widget = QTabWidget()

        self.user_page = self.init_users_page()
        self.test_page = self.init_tests_page()

        self.tab_widget.addTab(self.test_page, "Тесты")
        self.tab_widget.addTab(self.user_page, "Сотрудники")

        self.container.addWidget(self.tab_widget)
        self.show()



    def init_users_page(self):
        self.user_page_widget = QWidget()
        self.users_labels_layout = QVBoxLayout()

        for user in self.users:
            user_row = Item(f'{user["name"]}', user["id"])
            user_row.clicked.connect(partial(self.label_user_pushed, user_row))
            self.users_labels_layout.addWidget(user_row)

        self.user_page_widget.setLayout(self.users_labels_layout)
        return self.user_page_widget

    def init_tests_page(self):
        self.test_page_widget = QWidget()
        self.tests_labels_layout = QVBoxLayout()

        for test in self.tests:
            test_row = Item(f'{test["name"]}: {len(test["questions"])} вопроса', test["id"])
            test_row.clicked.connect(partial(self.label_test_pushed, test_row))
            self.tests_labels_layout.addWidget(test_row)

        self.test_page_widget.setLayout(self.tests_labels_layout)
        return self.test_page_widget

    def label_user_pushed(self, pushed_label):
        print(f"{pushed_label.id}")

    def label_test_pushed(self, pushed_label):
        print(f"{pushed_label.id}")


if __name__ == '__main__':
    app = QApplication([])
    tests = get_all_tests()
    users = get_users()
    auth_obj = Admin_view_tests_and_users(tests=tests, users=users)

    app.exec_()