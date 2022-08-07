from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit
from test_data_funcs import get_users
from PyQt5.QtCore import Qt
from Custom_Widgets.CollapsibleBox import CollapsibleBox
class Admin_user_view(QWidget):

    def __init__(self, user={}, parent=None):
        super(QWidget, self).__init__(parent)
        self.user = user
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        with open("Admin_user_view.css") as css:
            self.setStyleSheet(css.read())

        self.container = QVBoxLayout(self)

        self.name_label = QLabel("Имя сотрудника: ")
        self.container.addWidget(self.name_label)
        self.name_input_label = QLineEdit(self.user["name"])
        self.container.addWidget(self.name_input_label)


        self.password_label = QLabel("Пароль сотрудника: ")
        self.container.addWidget(self.password_label)
        self.password_input_label = QLineEdit(self.user["password"])
        self.container.addWidget(self.password_input_label)

        self.post_label = QLabel("Должность сотрудника: ")
        self.container.addWidget(self.post_label)
        self.post_input_label = QLineEdit(self.user["post"])
        self.container.addWidget(self.post_input_label)

        self.solved_test_label = QLabel("Решённые тесты: ")
        self.container.addWidget(self.solved_test_label)

        for i in self.user["tests"]:
            self.container.addWidget(self.init_layout_of_solved_test(i))

        self.container.addWidget(self)
        self.setLayout(self.container) # test thing
        self.show()

    def init_layout_of_solved_test(self, test):
        self.test_widget = QWidget()

        self.test_widget_layout =  QVBoxLayout()

        self.name_label = QLabel(f'Имя теста: {test["name"]}')
        self.test_widget_layout.addWidget(self.name_label)

        self.theme_label = QLabel(f'Тема теста: {test["theme"]}')
        self.test_widget_layout.addWidget(self.theme_label)

        self.result_label = QLabel(f'Результат теста: {test["result"]}/{test["max_result"]}')
        self.test_widget_layout.addWidget(self.result_label)

        self.box_for_wrong_questions = CollapsibleBox(title="Вопросы: ")
        self.box_for_wrong_questions_layout = QVBoxLayout()
        for i in test["test"]:
            self.box_for_wrong_questions_layout.addWidget(self.init_question_widget(i))
        self.box_for_wrong_questions_layout.setAlignment(Qt.AlignTop)
        self.box_for_wrong_questions.setContentLayout(self.box_for_wrong_questions_layout)
        self.test_widget_layout.addWidget(self.box_for_wrong_questions)


        # self.variants_of_answer_widget = QWidget()
        # self.variants_of_answer_layout = QVBoxLayout()
        # for variant in question["variants_of_answer"]:
        #     variant_of_answer_label = QLineEdit(variant)
        #     self.variants_of_answer_layout.addWidget(variant_of_answer_label)
        # self.variants_of_answer_widget.setLayout(self.variants_of_answer_layout)
        #
        # self.test_widget_layout.addWidget(self.variants_of_answer_widget)

        self.test_widget.setLayout(self.test_widget_layout)
        return self.test_widget

    def init_question_widget(self, question):
        self.solved_test_question_widget = QWidget()
        self.solved_test_question_widget_layout = QVBoxLayout()

        self.solved_test_question_label = QLabel(question["question"])
        self.solved_test_question_widget_layout.addWidget(self.solved_test_question_label)

        self.solved_test_question_widget.setLayout(self.solved_test_question_widget_layout)

        return self.solved_test_question_widget


if __name__ == '__main__':
    app = QApplication([])
    user = get_users()[0]
    auth_obj = Admin_user_view(user)
    # auth_obj = Admin_test_view()

    app.exec_()