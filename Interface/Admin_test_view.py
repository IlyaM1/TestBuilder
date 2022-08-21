from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QMainWindow
from PyQt5.QtCore import Qt
from test_data_funcs import get_all_tests
from Custom_Widgets.LineEdit_with_explanation import LineEdit_with_explanation
from Custom_Widgets.Button_with_information import Button_with_information
from Custom_Widgets.Deletable_TextInput import Deletable_TextInput
from Custom_Widgets.Deletable_LineEdit_with_explanation import Deletable_LineEdit_with_explanation
from Custom_Widgets.Question_widget_with_array_of_labels import Question_widget_with_array_of_labels
from config import Config
from copy import deepcopy
class Admin_test_view(QMainWindow):
    """
        Окошко для изменения и создания теста
        """
    def __init__(self, test={}, parent=None):
        super(QWidget, self).__init__(parent)
        self.EMPTY_QUESTION = {"question": "", "type": 1, "variants_of_answer": [], "answer": "", "balls": 0}
        self.test = test
        if self.test == {}:
            self.test = {"id": 0, "name": "", "theme": ""}
        self.all_widgets_questions = []
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        with open(Config().config["path"] + '\\Interface\\css\\Admin_test_view.css') as css:
            self.setStyleSheet(css.read())
        self.scroll_widget = QScrollArea()
        self.container_widget = QWidget()
        self.container = QVBoxLayout(self)

        self.constant_widget = QWidget()
        self.constant_layout = QVBoxLayout()

        self.name_label = QLabel("Имя теста: ")
        self.constant_layout.addWidget(self.name_label)

        self.name_input_label = QLineEdit(self.test["name"])
        self.constant_layout.addWidget(self.name_input_label)


        self.theme_label = QLabel("Тема теста: ")
        self.constant_layout.addWidget(self.theme_label)

        self.theme_input_label = QLineEdit(self.test["theme"])
        self.constant_layout.addWidget(self.theme_input_label)

        self.constant_widget.setLayout(self.constant_layout)
        self.container.addWidget(self.constant_widget)

        self.question_widget = QWidget()
        self.question_layout = QVBoxLayout()

        self.question_label = QLabel("Вопросы: ")
        self.question_layout.addWidget(self.question_label)

        self.question_widget_without_button = QWidget()
        self.question_layout_without_button = QVBoxLayout()

        current_numb_of_questions = 1
        for i in self.test["questions"]:

            question_widget_generated = self.init_layout_of_question(i, current_numb_of_questions)
            self.all_widgets_questions.append(question_widget_generated)
            self.question_layout_without_button.addWidget(question_widget_generated)
            current_numb_of_questions += 1

        self.question_widget_without_button.setLayout(self.question_layout_without_button)
        self.question_layout.addWidget(self.question_widget_without_button)

        self.new_question_button = QPushButton("Добавить вопрос")
        self.new_question_button.released.connect(self.new_question_button_released)
        self.question_layout.addWidget(self.new_question_button)

        self.question_widget.setLayout(self.question_layout)
        self.container.addWidget(self.question_widget)

        self.save_test_button = QPushButton("Сохранить тест")
        self.save_test_button.released.connect(self.save_button_released)
        self.container.addWidget(self.save_test_button)

        # self.container.addWidget(self)
        self.container_widget.setLayout(self.container)

        self.scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_widget.setWidgetResizable(True)
        self.scroll_widget.setWidget(self.container_widget)

        self.setCentralWidget(self.scroll_widget)
        self.show()

    def init_layout_of_question(self, question, number_of_question):
        self.one_question_widget = Question_widget_with_array_of_labels()

        self.one_question_layout =  QVBoxLayout()


        self.one_question_label = Deletable_LineEdit_with_explanation("Вопрос", question["question"], Config().config["path"] + "\\Interface\\Trash_Bin.png")
        self.one_question_widget.question_input = self.one_question_label.line_edit
        self.one_question_label.delete_button.released.connect(lambda: self.one_question_label_delete_button_pushed(number_of_question))
        self.one_question_layout.addWidget(self.one_question_label)

        self.variants_of_answer_label = QLabel("Варианты ответа: ")
        self.one_question_layout.addWidget(self.variants_of_answer_label)

        self.variants_of_answer_widget = QWidget()
        self.variants_of_answer_layout = QVBoxLayout()
        for variant in question["variants_of_answer"]:
            variant_of_answer_label = Deletable_TextInput(variant, Config().config["path"] + "\\Interface\\red_cross_delete.png")
            variant_of_answer_label.delete_button.released.connect(lambda: self.variant_of_answer_label_delete_button_pushed(variant, number_of_question))
            variant_of_answer_label.setObjectName('variant_of_answer_label')
            self.one_question_widget.array_of_labels.append(variant_of_answer_label.text_input)
            self.variants_of_answer_layout.addWidget(variant_of_answer_label)

        self.add_new_variant_button = Button_with_information("Добавить новый вариант ответа", "45")
        self.add_new_variant_button.clicked.connect(lambda: self.add_new_variant_button_pushed(number_of_question))
        self.variants_of_answer_layout.addWidget(self.add_new_variant_button)


        self.variants_of_answer_widget.setLayout(self.variants_of_answer_layout)

        self.one_question_layout.addWidget(self.variants_of_answer_widget)

        self.correct_answer = LineEdit_with_explanation("Правильный ответ", str(question["answer"]))
        self.one_question_widget.answer_input = self.correct_answer.line_edit
        self.one_question_layout.addWidget(self.correct_answer)

        self.number_of_balls = LineEdit_with_explanation("Количество баллов", str(question["balls"]))
        self.one_question_widget.ball_input = self.number_of_balls.line_edit
        self.one_question_layout.addWidget(self.number_of_balls)

        self.one_question_widget.setLayout(self.one_question_layout)
        return self.one_question_widget

    def new_question_button_released(self):
        self.test["questions"].append(deepcopy(self.EMPTY_QUESTION))
        current_number_of_questions = len(self.test["questions"])
        question_widget_generated = self.init_layout_of_question(deepcopy(self.EMPTY_QUESTION), current_number_of_questions)
        self.all_widgets_questions.append(question_widget_generated)
        self.question_layout_without_button.insertWidget(current_number_of_questions - 1, question_widget_generated)

    def save_button_released(self):
        print("saved") # TODO: save test in Database
        self.close()

    def add_new_variant_button_pushed(self, number_of_question):
        self.check_all_inputs_of_question(number_of_question)
        self.test["questions"][number_of_question-1]["variants_of_answer"].append("")
        self.question_layout_without_button.removeWidget(self.all_widgets_questions[number_of_question - 1])
        widget_generated = self.init_layout_of_question(self.test["questions"][number_of_question-1], number_of_question)
        self.all_widgets_questions[number_of_question-1] = widget_generated
        self.question_layout_without_button.insertWidget(number_of_question-1, widget_generated)

    def variant_of_answer_label_delete_button_pushed(self, variant, number_of_question):
        self.check_all_inputs_of_question(number_of_question)
        self.test["questions"][number_of_question-1]["variants_of_answer"].remove(variant)
        self.question_layout_without_button.removeWidget(self.all_widgets_questions[number_of_question-1])
        question_widget_generated = self.init_layout_of_question(self.test["questions"][number_of_question-1], number_of_question)
        self.all_widgets_questions[number_of_question-1] = question_widget_generated
        self.question_layout_without_button.insertWidget(number_of_question - 1, question_widget_generated)

    def one_question_label_delete_button_pushed(self, number_of_question):
        self.check_all_inputs_of_question(number_of_question)
        self.test["questions"].pop(number_of_question-1)
        self.question_layout_without_button.removeWidget(self.all_widgets_questions[number_of_question-1])
        self.all_widgets_questions = []
        self.init_UI()

    def check_all_inputs_of_question(self, number_of_question):
        self.test["questions"][number_of_question-1]["question"] = self.all_widgets_questions[number_of_question-1].question_input.text()
        self.test["questions"][number_of_question-1]["answer"] = self.all_widgets_questions[number_of_question-1].answer_input.text()
        self.test["questions"][number_of_question-1]["balls"] = int(self.all_widgets_questions[number_of_question - 1].ball_input.text())
        for i in range(len(self.test["questions"][number_of_question-1]["variants_of_answer"])):
            self.test["questions"][number_of_question - 1]["variants_of_answer"][i] = self.all_widgets_questions[number_of_question - 1].array_of_labels[i].text()



if __name__ == '__main__':
    app = QApplication([])
    test = get_all_tests()[0]
    auth_obj = Admin_test_view(test)

    app.exec_()