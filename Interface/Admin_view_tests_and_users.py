from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtCore import QSize, Qt
from Custom_Widgets.Clickable_label_with_delete_buttons import Clickable_label_with_delete_buttons
from test_data_funcs import get_all_tests, get_users
from functools import partial
from Interface.Admin_user_view import Admin_user_view
from Interface.Admin_test_view import Admin_test_view
from db.sqlite import SQLInteract
from config import Config


class Admin_view_tests_and_users(QWidget):
    """
    Окошко для просмотра всех тестов и юзеров адмном
    """

    def __init__(self, tests=[], users=[], parent=None):
        super(QWidget, self).__init__(parent)
        self.tests = tests
        self.users = users
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)
        with open(Config().config["path"] + '\\Interface\\css\\Admin_view_tests_and_users.css') as css:
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
        self.user_page_widget = QWidget()
        self.user_page_widget_layout = QVBoxLayout()

        self.user_page_scroll_widget = QScrollArea()
        self.users_labels_layout_widget = QWidget()
        self.users_labels_layout = QVBoxLayout()

        for user in self.users:
            user_row = Clickable_label_with_delete_buttons(f'{user["name"]}', user)
            user_row.setFixedSize(self.width() - 60, 50)
            user_row.label.clicked.connect(partial(self.label_user_pushed, user_row))
            self.users_labels_layout.addWidget(user_row)

        self.users_labels_layout_widget.setLayout(self.users_labels_layout)
        self.user_page_scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.user_page_scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.user_page_scroll_widget.setWidgetResizable(True)
        self.user_page_scroll_widget.setWidget(self.users_labels_layout_widget)
        self.user_page_widget_layout.addWidget(self.user_page_scroll_widget)

        self.new_user_button = QPushButton("Добавить сотрудника")
        self.new_user_button.released.connect(self.new_user_button_pushed)
        self.user_page_widget_layout.addWidget(self.new_user_button)

        self.user_page_widget.setLayout(self.user_page_widget_layout)

        return self.user_page_widget

    def init_tests_page(self):
        self.test_page_widget = QWidget()
        self.test_page_widget_layout = QVBoxLayout()

        self.test_page_scroll_widget = QScrollArea()
        self.tests_labels_layout_widget = QWidget()
        self.tests_labels_layout = QVBoxLayout()

        for test in self.tests:
            test_row = Clickable_label_with_delete_buttons(f'{test["name"]}: {len(test["questions"])} вопроса', test)
            test_row.setFixedSize(self.width() - 60, 50)
            test_row.label.clicked.connect(partial(self.label_test_pushed, test_row))
            self.tests_labels_layout.addWidget(test_row)

        self.tests_labels_layout_widget.setLayout(self.tests_labels_layout)
        self.test_page_scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.test_page_scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.test_page_scroll_widget.setWidgetResizable(True)
        self.test_page_scroll_widget.setWidget(self.tests_labels_layout_widget)
        self.test_page_widget_layout.addWidget(self.test_page_scroll_widget)

        self.new_test_button = QPushButton("Добавить тест")
        self.new_test_button.released.connect(self.new_test_button_pushed)
        self.test_page_widget_layout.addWidget(self.new_test_button)
        self.test_page_widget.setLayout(self.test_page_widget_layout)

        return self.test_page_widget

    def label_user_pushed(self, pushed_label):
        self.user_view = Admin_user_view(user=pushed_label.dictionary)

    def label_test_pushed(self, pushed_label):
        self.test_view = Admin_test_view(test=pushed_label.dictionary)

    def new_user_button_pushed(self):
        new_user = self.create_new_user()
        self.user_view = Admin_user_view(user=new_user)

    def new_test_button_pushed(self):
        new_test = self.create_new_test()
        self.test_view = Admin_test_view(test=new_test)

    def create_new_test(self):
        # TODO: this func creates new EMPTY test
        EMPTY_TEST = {
            "id": 100,
            "name": "",
            "theme": "",  # не меняй это образцы, если придется то и меня проверку в admin_test_view
            "max_result": -1,  # если тест новый, то max_result = -1, чтобы выставить new_test_flag
            "questions": []}  # Example
        return EMPTY_TEST

    def create_new_user(self):
        # TODO: this func creates new EMPTY user
        EMPTY_USER = {
            "id": 100,
            "name": "",
            "password": "",
            "post": "",  # Example
            "tests": []}  # не меняй это образцы, если придется то и меня проверку в admin_user_view
        return EMPTY_USER

    def get_user_by_id(self, id):
        pass


if __name__ == '__main__':
    cfg = Config()
    app = QApplication([])
    test = get_all_tests()[0]
    tests = [test for i in range(50)]
    user = get_users()[0]
    user_table = SQLInteract(table_name='testcase', filename_db=cfg.config["path"] + "/db/users.db")
    # user_table.sql_delete_one(need_value_of_name=1)
    # print(user_table.return_full_table())
    users = user_table.return_full_table(to_dict=True)
    # users = [user for i in range(20)]
    # TODO: продумать, инициализировать и привязать таблицу тестов
    auth_obj = Admin_view_tests_and_users(tests=tests, users=users)

    app.exec_()
