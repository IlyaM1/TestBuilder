from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QMainWindow
from test_data_funcs import get_users
from PyQt5.QtCore import Qt
from Custom_Widgets.CollapsibleBox import CollapsibleBox
# from db.sqlite import SQLInteract
# from db.hash import hash_password


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

        with open("css/Admin_user_view.css") as css:
            self.setStyleSheet(css.read())

        self.scroll_widget = QScrollArea()
        self.central_widget = QWidget()
        self.container = QVBoxLayout(self)

        self.constant_widget = QWidget()
        self.constant_widget_layout = QVBoxLayout()

        self.name_label = QLabel("Имя сотрудника: ")
        self.constant_widget_layout.addWidget(self.name_label)
        self.name_input_label = QLineEdit(self.user["name"])
        self.constant_widget_layout.addWidget(self.name_input_label)

        self.password_label = QLabel("Пароль сотрудника: ")
        self.constant_widget_layout.addWidget(self.password_label)
        self.password_input_label = QLineEdit(self.user["password"])
        self.password_input_label.setEchoMode(QLineEdit.Password)
        self.constant_widget_layout.addWidget(self.password_input_label)

        self.post_label = QLabel("Должность сотрудника: ")
        self.constant_widget_layout.addWidget(self.post_label)
        self.post_input_label = QLineEdit(self.user["post"])
        self.constant_widget_layout.addWidget(self.post_input_label)



        self.constant_widget.setLayout(self.constant_widget_layout)
        self.container.addWidget(self.constant_widget)

        if self.user["tests"] not in [None, False, []]:
            self.solved_test_widget = QWidget()
            self.solved_test_layout = QVBoxLayout()

            self.solved_test_label = QLabel("Решённые тесты: ")
            self.solved_test_layout.addWidget(self.solved_test_label)

            for i in self.user["tests"]:
                self.solved_test_layout.addWidget(self.init_layout_of_solved_test(i))

            self.solved_test_widget.setLayout(self.solved_test_layout)
            self.container.addWidget(self.solved_test_widget)
        else:
            self.solved_test_widget = QWidget()
            self.solved_test_layout = QVBoxLayout()

            self.solved_test_label = QLabel("Решённые тесты отсутствуют")
            self.solved_test_layout.addWidget(self.solved_test_label)
            self.solved_test_widget.setLayout(self.solved_test_layout)
            self.container.addWidget(self.solved_test_widget)



        self.save_user_button = QPushButton("Сохранить")
        self.save_user_button.clicked.connect(self.save_user_button_pushed)
        self.container.addWidget(self.save_user_button)

        self.central_widget.setLayout(self.container)

        self.scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_widget.setWidgetResizable(True)
        self.scroll_widget.setWidget(self.central_widget)

        self.setCentralWidget(self.scroll_widget)
        self.show()

    def init_layout_of_solved_test(self, test):
        self.test_widget = QWidget()

        self.test_widget_layout = QVBoxLayout()

        self.name_label = QLabel(f'Имя теста: {test["name"]}')
        self.test_widget_layout.addWidget(self.name_label)

        self.theme_label = QLabel(f'Тема теста: {test["theme"]}')
        self.test_widget_layout.addWidget(self.theme_label)

        self.result_label = QLabel(f'Результат теста: {test["result"]}/{test["max_result"]}')
        self.test_widget_layout.addWidget(self.result_label)

        self.box_for_wrong_questions = CollapsibleBox(title="Вопросы: ")
        self.box_for_wrong_questions_layout = QVBoxLayout()
        for i in test["test"]:
            if i["answer"] != i["key"] or True:
                self.box_for_wrong_questions_layout.addWidget(self.init_question_widget(i))
        self.box_for_wrong_questions_layout.setAlignment(Qt.AlignTop)
        self.box_for_wrong_questions.setContentLayout(self.box_for_wrong_questions_layout)
        self.test_widget_layout.addWidget(self.box_for_wrong_questions)

        self.test_widget.setLayout(self.test_widget_layout)
        return self.test_widget

    def init_question_widget(self, question):
        self.solved_test_question_widget = QWidget()
        self.solved_test_question_widget_layout = QVBoxLayout()

        self.solved_test_question_label = QLabel(f'Вопрос: {question["question"]}')
        self.solved_test_question_widget_layout.addWidget(self.solved_test_question_label)

        self.solved_test_answer_label = QLabel(f'Ответ/Правильный ответ: {question["answer"]}/{question["key"]}')
        self.solved_test_question_widget_layout.addWidget(self.solved_test_answer_label)

        self.solved_test_question_widget.setLayout(self.solved_test_question_widget_layout)

        return self.solved_test_question_widget

    def save_user_button_pushed(self):
        input_name = self.name_input_label.text().strip()
        input_password = self.password_input_label.text()
        input_post = self.post_input_label.text()
        input_password = str(hash_password(input_password))
        print(input_password)


        user_db = SQLInteract(table_name='testcase', filename_db='../db/users.db')
        # TODO: путь может сломаться если запускать из main.py issue #45
        user_db.sql_update_one_by_id(update_field="name", update_value="" + input_name + "", search_id=self.user["id"])
        user_db.sql_update_one_by_id(update_field="password", update_value=input_password, search_id=self.user["id"])
        user_db.sql_update_one_by_id(update_field="post", update_value=input_post, search_id=self.user["id"])

        # self.user
        print('Yay')


if __name__ == '__main__':
#     test_db = SQLInteract(table_name='testcase', filename_db='../db/users.db')
    app = QApplication([])
    user = get_users()[0]
#     print(test_db.return_full_table(to_dict=True))
#     user = test_db.sql_get_user_with_id(2)
    # test_db.sql_update_one_by_id(update_field="password", update_value="ersg", search_id=2)
    # print(test_db.return_full_table())
    # print(user)
    # user["tests"] = None
    # for i in range(20):
    #     user["tests"].append(user["tests"][0])
    auth_obj = Admin_user_view(user=user)

    app.exec_()