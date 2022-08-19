from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize, Qt
from test_data_funcs import get_all_tests

class Solving_test_widget(QMainWindow):
    """
    Окошко для выполнения теста
    """
    def __init__(self, test = {}, parent=None):
        super(QWidget, self).__init__(parent)
        self.test = test
        self.current_question = 1 # 1st question of test is №1
        self.number_of_all_questions = len(self.test["questions"])
        self.answers_to_all_questions = [""] * self.number_of_all_questions
        self.all_inputs_widgets = [QLineEdit()] * self.number_of_all_questions
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        with open('css/Solving_test_widget.css') as css:
            self.css_file = css.read()
            self.setStyleSheet(self.css_file)

        self.main_widget = QWidget()
        self.main_vertical_layout = QVBoxLayout()

        self.question_counter = QLabel(f"{self.current_question}/{self.number_of_all_questions} вопрос")
        self.question_counter.setObjectName("question_counter")
        self.main_vertical_layout.addWidget(self.question_counter)

        self.main_vertical_layout.addSpacing(50)

        question = self.test["questions"][self.current_question-1]
        self.current_question_widget = self.generate_question_layout(question, self.answers_to_all_questions[self.current_question-1])
        self.current_question_widget.setObjectName("current_question_widget")
        self.main_vertical_layout.addWidget(self.current_question_widget)

        self.buttons_horizontal_layout_widget = QWidget() # wrapper for buttons_horizontal_layout
        self.buttons_horizontal_layout = QHBoxLayout()

        self.backward_button = QPushButton("Назад")
        self.backward_button.released.connect(self.backward_button_pushed)
        self.buttons_horizontal_layout.addWidget(self.backward_button)

        self.next_button = QPushButton("Сохранить ответ и перейти к следующему вопросу")
        self.next_button.released.connect(self.next_button_pushed)
        self.buttons_horizontal_layout.addWidget(self.next_button)

        self.buttons_horizontal_layout_widget.setLayout(self.buttons_horizontal_layout)
        self.main_vertical_layout.addWidget(self.buttons_horizontal_layout_widget)

        self.main_widget.setLayout(self.main_vertical_layout)
        self.setCentralWidget(self.main_widget)

        self.show()

    def generate_question_layout(self, question, answer):
        self.question_widget = QWidget()
        self.question_widget_layout = QVBoxLayout()

        self.question_text_label = QLabel(question["question"])
        # self.question_text_label.setFixedHeight(100)
        self.question_widget_layout.addWidget(self.question_text_label)

        if len(question["variants_of_answer"]) == 0:
            self.answer_input_label = QLineEdit(answer)
            self.all_inputs_widgets[self.test["questions"].index(question)] = self.answer_input_label
            self.question_widget_layout.addWidget(self.answer_input_label)
        else:
            self.variants_of_answer_widget = QWidget()
            self.variants_of_answer_widget.setObjectName("variants_of_answer_widget")
            self.variants_of_answer_layout = QVBoxLayout()

            for variant in question["variants_of_answer"]:
                variant_of_answer_label = QLabel(variant)
                self.variants_of_answer_layout.addWidget(variant_of_answer_label)

            self.variants_of_answer_widget.setLayout(self.variants_of_answer_layout)
            self.question_widget_layout.addWidget(self.variants_of_answer_widget)

            self.answer_input_label = QLineEdit(answer)
            self.all_inputs_widgets[self.test["questions"].index(question)] = self.answer_input_label
            self.question_widget_layout.addWidget(self.answer_input_label)

        self.question_widget.setLayout(self.question_widget_layout)
        return self.question_widget

    def backward_button_pushed(self):
        if self.current_question == 1:
            return -1
        self.check_input(self.current_question - 1)
        self.current_question -= 1
        self.main_vertical_layout.removeWidget(self.current_question_widget)
        question = self.test["questions"][self.current_question - 1]
        self.current_question_widget = self.generate_question_layout(question, self.answers_to_all_questions[self.current_question - 1])
        self.current_question_widget.setObjectName("current_question_widget")
        self.main_vertical_layout.insertWidget(1, self.current_question_widget)
        self.question_counter.setText(f"{self.current_question}/{self.number_of_all_questions} вопрос")
        self.next_button.setText("Сохранить ответ и перейти к следующему вопросу")
        self.setStyleSheet(self.css_file)

    def next_button_pushed(self):
        if self.current_question == self.number_of_all_questions:
            self.finish_and_save_test()
            return
        self.check_input(self.current_question - 1)
        self.current_question += 1
        self.main_vertical_layout.removeWidget(self.current_question_widget)
        question = self.test["questions"][self.current_question - 1]
        self.current_question_widget = self.generate_question_layout(question, self.answers_to_all_questions[self.current_question - 1])
        self.current_question_widget.setObjectName("current_question_widget")
        self.main_vertical_layout.insertWidget(1, self.current_question_widget)
        self.question_counter.setText(f"{self.current_question}/{self.number_of_all_questions} вопрос")
        if self.current_question == self.number_of_all_questions:
            self.next_button.setText("Завершить и сохранить тест")
        else:
            self.next_button.setText("Сохранить ответ и перейти к следующему вопросу")
        self.setStyleSheet(self.css_file)

    def check_input(self, current_question):
        self.answers_to_all_questions[current_question] = self.all_inputs_widgets[current_question].text()
    def finish_and_save_test(self):
        print("finish_and_save_test")


if __name__ == '__main__':
    app = QApplication([])
    test = get_all_tests()[0]
    solve_test = Solving_test_widget(test=test)

    app.exec_()

#margin-bottom: 50px;