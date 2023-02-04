from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QMainWindow
from test_data_funcs import get_users
from PyQt5.QtCore import Qt
from Custom_Widgets.CollapsibleBox import CollapsibleBox
from db.sqlite import SQLInteract
from db.hash import hash_password
from config import Config


class Admin_user_view(QMainWindow):
    """
    Окошко для изменения и создания юзера
    """
    def __init__(self, user={}, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.user = user
        if self.user == {}:
            self.user = {"id": 0, "name": '', "password": '', "post": '', "tests": []}
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)
        self.set_css()

        self.container = QVBoxLayout(self)

        self.constant_widget = self.generate_constant_widget()
        self.container.addWidget(self.constant_widget)

        self.solved_test_widget = self.generate_solved_test_widget(self.user["tests"])
        self.container.addWidget(self.solved_test_widget)

        self.save_user_button = self.generate_button_with_slot("Сохранить", self.save_user_button_pushed)
        self.container.addWidget(self.save_user_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.container)

        scroll_widget = self.generate_scroll_widget(self.central_widget)
        self.setCentralWidget(scroll_widget)

        self.show()

    def set_css(self):
        with open(Config().config["path"] + '\\Interface\\css\\Admin_user_view.css') as css:
            self.setStyleSheet(css.read())

    def generate_constant_widget(self):
        constant_widget = QWidget()
        constant_widget_layout = QVBoxLayout()

        self.name_input_label = self.generate_and_add_label_with_input("Имя сотрудника: ", self.user["name"],
                                                                       constant_widget_layout)
        self.password_input_label = self.generate_and_add_label_with_input("Пароль сотрудника: ", self.user["password"],
                                                                           constant_widget_layout)
        self.post_input_label = self.generate_and_add_label_with_input("Должность сотрудника: ", self.user["post"],
                                                                       constant_widget_layout)

        constant_widget.setLayout(constant_widget_layout)
        return constant_widget

    def generate_solved_test_widget(self, tests):
        solved_test_widget = QWidget()
        solved_test_layout = QVBoxLayout()

        if tests not in [None, False, []]:
            solved_test_label = QLabel("Решённые тесты: ")
            solved_test_layout.addWidget(solved_test_label)

            for test in tests:
                solved_test_layout.addWidget(self.init_layout_of_solved_test(test))

            solved_test_widget.setLayout(solved_test_layout)
        else:
            solved_test_label = QLabel("Решённые тесты отсутствуют")
            solved_test_layout.addWidget(solved_test_label)
            solved_test_widget.setLayout(solved_test_layout)

        solved_test_scroll_area = Admin_user_view.generate_scroll_widget(solved_test_widget)
        return solved_test_scroll_area

    @staticmethod
    def init_layout_of_solved_test(test):
        test_widget_layout = QVBoxLayout()
        Admin_user_view.generate_label_add_to_widget(f'Имя теста: {test["name"]}', test_widget_layout)
        Admin_user_view.generate_label_add_to_widget(f'Тема теста: {test["theme"]}', test_widget_layout)
        Admin_user_view.generate_label_add_to_widget(f'Результат теста: {test["result"]}/{test["max_result"]}', test_widget_layout)

        box_for_wrong_questions = CollapsibleBox(title="Вопросы: ")
        box_for_wrong_questions_layout = QVBoxLayout()

        for question in test["test"]:
            if question["answer"] != question["key"] or True:
                box_for_wrong_questions_layout.addWidget(Admin_user_view.init_question_widget(question))

        box_for_wrong_questions_layout.setAlignment(Qt.AlignTop)
        box_for_wrong_questions.setContentLayout(box_for_wrong_questions_layout)
        test_widget_layout.addWidget(box_for_wrong_questions)

        test_widget = QWidget()
        test_widget.setLayout(test_widget_layout)
        return test_widget

    @staticmethod
    def init_question_widget(question):
        solved_test_question_widget = QWidget()
        solved_test_question_widget_layout = QVBoxLayout()

        solved_test_question_label = QLabel(f'Вопрос: {question["question"]}')
        solved_test_question_widget_layout.addWidget(solved_test_question_label)

        solved_test_answer_label = QLabel(f'Ответ/Правильный ответ: {question["answer"]}/{question["key"]}')
        solved_test_question_widget_layout.addWidget(solved_test_answer_label)

        solved_test_question_widget.setLayout(solved_test_question_widget_layout)
        return solved_test_question_widget

    @staticmethod
    def generate_label_add_to_widget(text, parent_widget):
        label = QLabel(text)
        parent_widget.addWidget(label)

    @staticmethod
    def generate_scroll_widget(widget_to_set):
        scroll_widget = QScrollArea()
        scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_widget.setWidgetResizable(True)
        scroll_widget.setWidget(widget_to_set)

        return scroll_widget

    @staticmethod
    def generate_button_with_slot(text, connect_function):
        button = QPushButton(text)
        button.clicked.connect(connect_function)

        return button

    @staticmethod
    def generate_and_add_label_with_input(label_text, input_text, parent_widget):
        label = QLabel(label_text)
        parent_widget.addWidget(label)
        input = QLineEdit(input_text)
        parent_widget.addWidget(input)

        return input

    @staticmethod
    def generate_and_add_label(text, parent_widget):
        name_label = QLabel(f'Имя теста: {text}')
        parent_widget.addWidget(name_label)

    def save_user_button_pushed(self):
        input_name = self.name_input_label.text().strip()
        input_password = self.password_input_label.text()
        input_post = self.post_input_label.text()
        # input_password = str(hash_password(input_password))
        input_password = str(input_password)
        print(input_password)

        cfg = Config()
        user_db = SQLInteract(table_name='testcase', filename_db=cfg.config["path"] + '/db/users.db')
        user_db.sql_update_one_by_id(update_field="name", update_value="" + input_name + "", search_id=self.user["id"])
        user_db.sql_update_one_by_id(update_field="password", update_value=input_password, search_id=self.user["id"])
        user_db.sql_update_one_by_id(update_field="post", update_value=input_post, search_id=self.user["id"])

        # self.user
        print('Yay')
        self.close()


if __name__ == '__main__':
    cfg = Config()
    test_db = SQLInteract(table_name='testcase', filename_db=cfg.config["path"] + '/db/users.db')
    app = QApplication([])
    user = get_users()[0]
    #     print(test_db.return_full_table(to_dict=True))
    #     user = test_db.sql_get_user_with_id(2)
    # test_db.sql_update_one_by_id(update_field="password", update_value="ersg", search_id=2)
    # print(test_db.return_full_table())
    # print(user)
    # user["tests"] = None
    for i in range(20):
        user["tests"].append(user["tests"][0])
    auth_obj = Admin_user_view(user=user)

    app.exec_()
