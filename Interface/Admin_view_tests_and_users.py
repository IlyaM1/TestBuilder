import json

from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtCore import QSize, Qt, pyqtSignal
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
        self.all_user_labels = []
        self.all_tests_labels = []
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)
        with open(Config().config["path"] + '\\Interface\\css\\Admin_view_tests_and_users.css') as css:
            self.setStyleSheet(css.read())

        container = QVBoxLayout(self)

        tab_widget = QTabWidget()

        user_page = self.init_users_page()
        test_page = self.init_tests_page()

        tab_widget.addTab(test_page, "Тесты")
        tab_widget.addTab(user_page, "Сотрудники")

        container.addWidget(tab_widget)
        self.show()

    def init_users_page(self):
        user_page_widget = QWidget()
        user_page_widget_layout = QVBoxLayout()

        users_labels_layout_widget = QWidget()
        self.users_labels_layout = QVBoxLayout()

        for user in self.users:
            user_row = self.create_row(user["name"], user, self.width() - 60, self.label_user_pushed)
            user_row.deleted_signal.connect(partial(self.delete_user_row, user["id"]))
            self.all_user_labels.append(user_row)
            self.users_labels_layout.addWidget(user_row)

        users_labels_layout_widget.setLayout(self.users_labels_layout)

        user_page_scroll_widget = self.generate_scroll_widget(users_labels_layout_widget)
        user_page_widget_layout.addWidget(user_page_scroll_widget)

        new_user_button = QPushButton("Добавить сотрудника")
        new_user_button.released.connect(self.create_new_user)
        user_page_widget_layout.addWidget(new_user_button)

        user_page_widget.setLayout(user_page_widget_layout)

        return user_page_widget

    def init_tests_page(self):
        test_page_widget = QWidget()
        test_page_widget_layout = QVBoxLayout()

        tests_labels_layout_widget = QWidget()
        self.tests_labels_layout = QVBoxLayout()

        for test in self.tests:
            question_quantity = len(test["questions"])
            test_row_name = f'{test["name"]}: {question_quantity} {self.generate_word_ending("вопрос", question_quantity)}'
            test_row = self.create_row(test_row_name, test, self.width() - 60, self.label_test_pushed)
            test_row.deleted_signal.connect(partial(self.delete_test_row, test["id"]))
            self.all_tests_labels.append(test_row)
            self.tests_labels_layout.addWidget(test_row)

        tests_labels_layout_widget.setLayout(self.tests_labels_layout)
        test_page_scroll_widget = self.generate_scroll_widget(tests_labels_layout_widget)
        test_page_widget_layout.addWidget(test_page_scroll_widget)

        new_test_button = QPushButton("Добавить тест")
        new_test_button.released.connect(self.new_test_button_pushed)
        test_page_widget_layout.addWidget(new_test_button)
        test_page_widget.setLayout(test_page_widget_layout)

        return test_page_widget

    @staticmethod
    def generate_scroll_widget(widget_to_set):
        scroll_widget = QScrollArea()

        scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_widget.setWidgetResizable(True)
        scroll_widget.setWidget(widget_to_set)

        return scroll_widget

    @staticmethod
    def create_row(name, dictionary, size, slot):
        row = Clickable_label_with_delete_buttons(name, dictionary)
        row.setFixedSize(size, 50)
        row.label.clicked.connect(partial(slot, row))

        return row

    def label_user_pushed(self, pushed_label):
        if isinstance(pushed_label.dictionary["tests"], str):
            pushed_label.dictionary["tests"] = json.loads(pushed_label.dictionary["tests"])

        self.user_view = Admin_user_view(user=pushed_label.dictionary)
        self.user_view.closed_signal.connect(
            partial(self.change_name_of_user_created_label, self.user_view))

    def find_user_row_index_with_id(self, id):
        for i in range(len(self.all_user_labels)):
            if self.all_user_labels[i].dictionary["id"] == id:
                return i
        raise Exception("Can't find user_row with that index")

    def find_test_row_index_with_id(self, id):
        for i in range(len(self.all_tests_labels)):
            if self.all_tests_labels[i].dictionary["id"] == id:
                return i
        raise Exception("Can't find test_row with that index")

    def label_test_pushed(self, pushed_label):
        if isinstance(pushed_label.dictionary["questions"], str):
            pushed_label.dictionary["questions"] = json.loads(pushed_label.dictionary["questions"])

        self.test_view = Admin_test_view(test=pushed_label.dictionary)
        self.test_view.closed_signal.connect(
            partial(self.change_name_of_test_created_label, self.test_view))

    def new_test_button_pushed(self):
        self.test_view = Admin_test_view(test={})

        new_test = self.test_view.test
        self.tests.append(new_test)

        question_quantity = len(new_test["questions"])
        test_row_name = f'{new_test["name"]}: {question_quantity} {self.generate_word_ending("вопрос", question_quantity)}'
        test_row = self.create_row(test_row_name, new_test, self.width() - 60, self.label_test_pushed)

        self.all_tests_labels.append(test_row)
        self.tests_labels_layout.addWidget(test_row)

        self.test_view.closed_signal.connect(
            partial(self.change_name_of_test_created_label, self.test_view))
        return True

    def create_new_user(self):
        self.user_view = Admin_user_view(user={})
        new_user = self.user_view.user
        self.users.append(new_user)

        user_row = self.create_row(new_user["name"], new_user, self.width() - 60, self.label_user_pushed)
        self.all_user_labels.append(user_row)
        self.users_labels_layout.addWidget(user_row)

        self.user_view.closed_signal.connect(
            partial(self.change_name_of_user_created_label, self.user_view))
        return True

    def change_name_of_user_created_label(self, user_view):
        user_id = user_view.user["id"]
        label_index = self.find_user_row_index_with_id(user_id)
        self.all_user_labels[label_index].deleted_signal.connect(partial(self.delete_user_row, user_id))

        user_name = self.all_user_labels[label_index].dictionary["name"]
        self.all_user_labels[label_index].label.setText(user_name)

    def change_name_of_test_created_label(self, test_view):
        test = test_view.test
        test_id = test["id"]
        label_index = self.find_test_row_index_with_id(test_id)
        self.all_tests_labels[label_index].deleted_signal.connect(partial(self.delete_test_row, test_id))
        self.all_tests_labels[label_index].label.setText(test["name"])

    def delete_user_row(self, id):
        user_row_index = self.find_user_row_index_with_id(id)

        self.users_labels_layout.removeWidget(self.all_user_labels[user_row_index])
        self.all_user_labels[user_row_index].deleteLater()
        self.all_user_labels.pop(user_row_index)

    def delete_test_row(self, id):
        test_row_index = self.find_test_row_index_with_id(id)

        self.tests_labels_layout.removeWidget(self.all_tests_labels[test_row_index])
        self.all_tests_labels[test_row_index].deleteLater()
        self.all_tests_labels.pop(test_row_index)

    @staticmethod
    def generate_word_ending(word, number):
        if 10 <= number % 100 < 20 or number % 10 > 4 or number % 10 == 0:
            return word + 'ов'
        elif number % 10 == 1:
            return word + ''
        else:
            return word + 'a'


if __name__ == '__main__':
    cfg = Config()
    app = QApplication([])
    # test = get_all_tests()[0]

    # user = get_users()[0]
    user_table = SQLInteract(table_name='testcase', filename_db=cfg.config["path"] + "/db/users.db")
    test_table = SQLInteract(table_name="tests", filename_db=cfg.config["path"] + "/db/users.db",
                             values_of_this_table="(id, name, theme, max_result, questions)",
                             init_values="(id int PRIMARY KEY, name text, theme text, max_result int, questions)")

    tests = test_table.return_full_table(to_dict=True, element_for_transform="questions")
    # user_table.sql_delete_one(need_value_of_name=1)
    # print(user_table.return_full_table())
    users = user_table.return_full_table(to_dict=True)
    # users = [user for i in range(20)]
    # TODO: продумать, инициализировать и привязать таблицу тестов
    auth_obj = Admin_view_tests_and_users(tests=tests, users=users)

    app.exec_()
