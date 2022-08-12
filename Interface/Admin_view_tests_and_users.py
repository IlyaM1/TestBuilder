from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtCore import QSize, Qt
from Custom_Widgets.Item import Item
from test_data_funcs import get_all_tests, get_users
from functools import partial
from db.sqlite import SQLInteract


from Interface.Admin_user_view import Admin_user_view
from Interface.Admin_test_view import Admin_test_view
from db.sqlite import SQLInteract


class Admin_view_tests_and_users(QWidget):

    def __init__(self, tests=[], users=[], parent=None):
        super(QWidget, self).__init__(parent)
        self.tests = tests
        self.users = users
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        with open('css/Admin_view_tests_and_users.css') as css:
            self.setStyleSheet(css.read())

        self.container = QVBoxLayout(self)

        self.tab_widget = QTabWidget()

        self.user_page = self.init_users_page()
        self.test_page = self.init_tests_page()

        self.tab_widget.addTab(self.test_page, "Тесты")
        self.tab_widget.addTab(self.user_page, "Сотрудники")

        self.container.addWidget(self.tab_widget)
        self.show()

    def init_users_page(self):
        self.user_page_scroll_widget = QScrollArea()
        self.user_page_widget = QWidget()
        self.users_labels_layout = QVBoxLayout()

        for user in self.users:
            user_row = Item(f'{user["name"]}', user["id"])
            user_row.setFixedSize(self.width() - 40, 120)
            user_row.clicked.connect(partial(self.label_user_pushed, user_row))
            self.users_labels_layout.addWidget(user_row)

        self.new_user_button = QPushButton("Добавить сотрудника")
        self.new_user_button.released.connect(self.new_user_button_pushed)
        self.users_labels_layout.addWidget(self.new_user_button)
        self.user_page_widget.setLayout(self.users_labels_layout)

        self.user_page_scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.user_page_scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.user_page_scroll_widget.setWidgetResizable(True)
        self.user_page_scroll_widget.setWidget(self.user_page_widget)

        return self.user_page_scroll_widget

    def init_tests_page(self):
        self.test_page_scroll_widget = QScrollArea()
        self.test_page_widget = QWidget()
        self.tests_labels_layout = QVBoxLayout()

        for test in self.tests:
            test_row = Item(f'{test["name"]}: {len(test["questions"])} вопроса', test["id"])
            test_row.setFixedSize(self.width() - 40, 120)
            test_row.clicked.connect(partial(self.label_test_pushed, test_row))
            self.tests_labels_layout.addWidget(test_row)

        self.new_test_button = QPushButton("Добавить тест")
        self.new_test_button.released.connect(self.new_test_button_pushed)
        self.tests_labels_layout.addWidget(self.new_test_button)
        self.test_page_widget.setLayout(self.tests_labels_layout)

        self.test_page_scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.test_page_scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.test_page_scroll_widget.setWidgetResizable(True)
        self.test_page_scroll_widget.setWidget(self.test_page_widget)

        return self.test_page_scroll_widget

    def label_user_pushed(self, pushed_label):
        self.close()
        # user = get_user_by_id(pushed_label.id) # @akrisfx
        user = self.users[0] # test thing
        print(user)
        self.user_view = Admin_user_view(user=user)

    def label_test_pushed(self, pushed_label):
        self.close()
        # test = get_test_by_id(pushed_label.id) # @akrisfx
        test = self.tests[0]  # test thing
        print(test)
        self.test_view = Admin_test_view(test=test)

    def new_user_button_pushed(self):
        self.close()
        self.create_new_user()
        self.user_view = Admin_user_view()

    def new_test_button_pushed(self):
        self.close()
        self.create_new_test()
        self.test_view = Admin_test_view()

    def create_new_test(self):
        # this func creates new EMPTY test
        pass

    def create_new_user(self):
        # this func creates new EMPTY user
        pass
    def get_user_by_id(self, id):
        pass

if __name__ == '__main__':
    app = QApplication([])
    test = get_all_tests()[0]
    tests = [test for i in range(50)]
    user = get_users()[0]
    user_table = SQLInteract(table_name='testcase')
    # user_table.sql_delete_one(need_value_of_name=1)
    print(user_table.return_full_table())
    users = user_table.return_full_table(to_dict=True)
    # users = [user for i in range(20)]
    # TODO: продумать, инициализировать и привязать таблицу тестов
    auth_obj = Admin_view_tests_and_users(tests=tests, users=users)

    app.exec_()
