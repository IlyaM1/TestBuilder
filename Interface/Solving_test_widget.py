from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from test_data_funcs import get_all_tests
from Interface.Ending_test_widget import Ending_test_widget
from config import Config
from db.sqlite import SQLInteract
import time
from copy import deepcopy
import db.user


class Solving_test_widget(QMainWindow):
    """
    Окошко для выполнения теста
    """

    def __init__(self, test={}, user={}, parent=None):
        super(QWidget, self).__init__(parent)
        self.test = test
        self.user = user
        self.config = Config()

        self.current_question = 1
        self.number_of_all_questions = len(self.test["questions"])

        self.answers_to_all_questions = [""] * self.number_of_all_questions
        self.all_types_of_questions = [0] * self.number_of_all_questions  # 1 - input_label, 2 - radiobox, 3 - checkbox
        self.all_inputs_widgets = [0] * self.number_of_all_questions  # TODO:

        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)
        self.setWindowTitle(self.test["name"])

        with open(Config().config["path"] + '\\Interface\\css\\Solving_test_widget.css') as css:
            self.css_file = css.read()
            self.setStyleSheet(self.css_file)

        self.main_vertical_layout = QVBoxLayout()

        self.question_counter = self.generate_question_counter()
        self.main_vertical_layout.addWidget(self.question_counter)

        self.current_question_widget = self.generate_question_widget()
        self.current_question_widget.setObjectName("current_question_widget")
        self.main_vertical_layout.addWidget(self.current_question_widget)

        self.buttons_widget = self.generate_buttons_widget()
        self.main_vertical_layout.addWidget(self.buttons_widget)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_vertical_layout)
        self.setCentralWidget(self.main_widget)

        self.show()

    def generate_question_counter(self):
        question_counter = QLabel(f"{self.current_question}/{self.number_of_all_questions} вопрос")
        question_counter.setObjectName("question_counter")
        question_counter.setMaximumHeight(10)
        return question_counter

    def generate_buttons_widget(self):
        self.buttons_widget = QWidget()  # wrapper for buttons_horizontal_layout
        self.buttons_horizontal_layout = QHBoxLayout()

        backward_button = QPushButton("Назад")
        backward_button.setMaximumWidth(200)
        backward_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # self.backward_button.contentsMargins().setRight()
        backward_button.released.connect(self.backward_button_pushed)
        self.buttons_horizontal_layout.addWidget(backward_button)

        self.next_button = QPushButton("Сохранить ответ и перейти к следующему вопросу")
        self.next_button.setObjectName("next_button")
        self.next_button.setFixedWidth(600)
        self.next_button.released.connect(self.next_button_pushed)
        self.buttons_horizontal_layout.addWidget(self.next_button)

        self.buttons_widget.setLayout(self.buttons_horizontal_layout)

        return self.buttons_widget

    def generate_question_widget(self):
        question_widget_layout = QVBoxLayout()

        scroll_area_question = self.generate_question_text_scroll_area()
        question_widget_layout.addWidget(scroll_area_question)

        question_widget_layout.addSpacing(20)
        variants_of_answer_widget = self.generate_variants_of_answer_widget()
        question_widget_layout.addWidget(variants_of_answer_widget)

        question_widget = QWidget()
        question_widget.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        question_widget.setLayout(question_widget_layout)

        return question_widget

    def generate_question_text_scroll_area(self):
        question_text_label = QLabel(self.test["questions"][self.current_question - 1]["question"])
        question_text_label.setObjectName("question_label")
        question_text_label.setMaximumWidth(self.width())
        question_text_label.setWordWrap(True)

        scroll_area_question = QScrollArea()
        scroll_area_question.setWidget(question_text_label)
        scroll_area_question.setObjectName("question_scrollarea")
        scroll_area_question.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area_question.setFixedHeight(300)
        scroll_area_question.setWidgetResizable(True)

        return scroll_area_question

    def generate_variants_of_answer_widget(self):
        variants_of_answer_widget = QWidget()
        variants_of_answer_widget.setObjectName("variants_of_answer_widget")
        variants_of_answer_layout = QVBoxLayout()

        if self.test["questions"][self.current_question - 1]["answer"] is None:
            self.all_types_of_questions[self.current_question - 1] = 1

            answer_input_label = QLineEdit()
            answer_input_label.setPlaceholderText("Ваш ответ")

            self.answers_to_all_questions[self.current_question - 1] = answer_input_label
            self.variants_of_answer_layout.addWidget(answer_input_label)


        elif isinstance(self.test["questions"][self.current_question - 1]["answer"], str) is True:
            self.all_types_of_questions[self.current_question - 1] = 2

            variants_of_answer_button_group = QButtonGroup()
            variants_of_answer_button_group_layout = QVBoxLayout()

            for variant in self.test["questions"][self.current_question - 1]["variants_of_answer"]:
                variant_of_answer_radio_button = QRadioButton(variant)
                variant_of_answer_radio_button.setObjectName("answer_option_label")
                variants_of_answer_button_group_layout.addWidget(variant_of_answer_radio_button)
                variants_of_answer_button_group.addButton(variant_of_answer_radio_button)

            # variants_of_answer_button_group.buttonClicked.connect(self.on_radio_button_clicked)
            self.all_inputs_widgets[self.current_question - 1] = variants_of_answer_button_group

            variants_of_answer_button_group_widget = QWidget()
            variants_of_answer_button_group_widget.setLayout(variants_of_answer_button_group_layout)

            scroll_area_answers = self.generate_scroll_area_answers(variants_of_answer_button_group_widget)
            variants_of_answer_layout.addWidget(scroll_area_answers)


        elif isinstance(self.test["questions"][self.current_question - 1]["answer"], list) is True:
            self.all_types_of_questions[self.current_question - 1] = 3
            self.answers_to_all_questions[self.current_question - 1] = []

            check_box_layout = QVBoxLayout()
            all_check_boxes = []

            for variant in self.test["questions"][self.current_question - 1]["variants_of_answer"]:
                variants_of_answer_check_box = QCheckBox(variant)
                variants_of_answer_check_box.setObjectName("answer_option_label")
                check_box_layout.addWidget(variants_of_answer_check_box)
                variants_of_answer_check_box.toggle()
                # variants_of_answer_check_box.stateChanged.connect(self.clicked_check_box)
                all_check_boxes.append(variants_of_answer_check_box)

            self.all_inputs_widgets[self.current_question - 1] = all_check_boxes
            check_box_widget = QWidget()
            check_box_widget.setLayout(check_box_layout)

            scroll_area_answers = self.generate_scroll_area_answers(check_box_widget)
            variants_of_answer_layout.addWidget(scroll_area_answers)

        variants_of_answer_widget.setLayout(variants_of_answer_layout)

        return variants_of_answer_widget

    def generate_scroll_area_answers(self, widget):
        scroll_area_answers = QScrollArea()
        scroll_area_answers.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area_answers.setWidget(widget)
        scroll_area_answers.setFixedHeight(150)
        scroll_area_answers.setWidgetResizable(True)
        return scroll_area_answers

    def backward_button_pushed(self):
        if self.current_question == 1:
            return -1
        self.check_input(self.current_question)
        self.current_question -= 1
        self.main_vertical_layout.removeWidget(self.current_question_widget)
        self.current_question_widget = self.generate_question_layout()
        self.current_question_widget.setObjectName("current_question_widget")
        self.main_vertical_layout.insertWidget(1, self.current_question_widget)
        self.question_counter.setText(f"{self.current_question}/{self.number_of_all_questions} вопрос")
        self.next_button.setText("Сохранить ответ и перейти к следующему вопросу")
        self.setStyleSheet(self.css_file)

    def next_button_pushed(self):
        if self.current_question == self.number_of_all_questions:
            self.finish_and_save_test()
            return
        self.check_input(self.current_question)
        self.current_question += 1
        self.main_vertical_layout.removeWidget(self.current_question_widget)
        self.current_question_widget = self.generate_question_widget()
        self.current_question_widget.setObjectName("current_question_widget")
        self.main_vertical_layout.insertWidget(1, self.current_question_widget)

        self.question_counter.setText(f"{self.current_question}/{self.number_of_all_questions} вопрос")

        if self.current_question == self.number_of_all_questions:
            self.next_button.setText("Завершить и сохранить тест")
        else:
            self.next_button.setText("Сохранить ответ и перейти к следующему вопросу")

        self.setStyleSheet(self.css_file)

    def check_input(self, current_question):
        if self.all_types_of_questions[current_question - 1] == 1:
            self.answers_to_all_questions[current_question - 1] = self.all_inputs_widgets[current_question - 1].text()
        elif self.all_types_of_questions[current_question - 1] == 2:
            self.answers_to_all_questions[current_question - 1] = self.all_inputs_widgets[current_question - 1].checkedButton().text()
        elif self.all_types_of_questions[current_question - 1] == 3:
            arr = []
            for check_box in self.all_inputs_widgets[current_question - 1]:
                if check_box.isChecked() is True:
                    arr.append(check_box.text())
            self.answers_to_all_questions[current_question - 1] = arr

        # self.answers_to_all_questions[current_question] = self.all_inputs_widgets[current_question].text()

    def finish_and_save_test(self):
        self.check_input(self.current_question - 1)
        # self.answers_to_all_questions - array that contains all answers(at 0 index - answer on 1st question of test etc)
        number_of_wrong_answers = self.count_wrong_answers()
        result = self.count_result()
        # print(number_of_wrong_answers, result, self.answers_to_all_questions, self.test)
        ready_test = self.generate_done_test(result)
        self.close()
        user_db = SQLInteract(table_name="testcase", filename_db=self.config.config["path"] + "/db/users.db")
        self.user["tests"].append(ready_test)
        self.user["tests"] = db.user.from_dict_to_str(self.user["tests"])
        # print(self.user)
        update_status = user_db.sql_update_one_by_id(update_field="tests", update_value=self.user["tests"],
                                                     search_id=self.user["id"])
        if not update_status:
            print('Чёта сломалось, обратитесь в службу поддержки E̷F̷T̷ TestBuilder`a')
            self.end_test_widget = Ending_test_widget(result=result, wrong_answers='Чёта сломалось, обратитесь в '
                                                                                   'службу поддержки E̷F̷T̷ '
                                                                                   'TestBuilder`a',
                                                      max_result=self.test["max_result"])
        else:
            self.end_test_widget = Ending_test_widget(result=result, wrong_answers=number_of_wrong_answers,
                                                      max_result=self.test["max_result"], user=self.user)
        # print(user_db.return_full_table(name_of_table="testcase", to_dict=True)[1])  # для дебага

    def count_result(self):
        result = 0
        for index_of_question in range(len(self.test["questions"])):
            if self.answers_to_all_questions[index_of_question] == self.test["questions"][index_of_question]["answer"]:
                result += self.test["questions"][index_of_question]["balls"]
        return result

    def count_wrong_answers(self):
        number_of_wrong_answers = 0
        for index_of_question in range(len(self.test["questions"])):
            if self.answers_to_all_questions[index_of_question] != self.test["questions"][index_of_question]["answer"]:
                number_of_wrong_answers += 1
        return number_of_wrong_answers

    def generate_done_test(self, result):
        rdy_test = deepcopy(self.test)
        rdy_test["result"] = result
        rdy_test["time"] = time.asctime(time.localtime(time.time()))
        # print(time.asctime(time.localtime(time.time())))
        for i, x in enumerate(self.answers_to_all_questions):
            rdy_test["questions"][i]["key"] = x
            if x == rdy_test["questions"][i]["answer"]:
                rdy_test["questions"][i]["points_awarded"] = rdy_test["questions"][i]["balls"]
            else:
                rdy_test["questions"][i]["points_awarded"] = 0
        return rdy_test

    def _on_radio_button_clicked(self, button):
        self.answers_to_all_questions[self.current_question - 1] = button.text()
        # print(button.text())


if __name__ == '__main__':
    app = QApplication([])
    test = get_all_tests()[0]
    solve_test = Solving_test_widget(test=test, user={'id': 3, 'name': 'ILYA2', 'password': "b'b8~\\xac)\\xe3A\\xc7"
                                                                                            "\\xe6\\xf6\\x8aI/P\\xee"
                                                                                            "\\xf5\\xeb\\x90\\x8cO"
                                                                                            "<\\xcb\\xbc\\xdd\\xc1"
                                                                                            "=\\xad\\xc4S\\xcdJ\\x16"
                                                                                            "\\xc07\\x8a("
                                                                                            "\\xc4\\x0c_#\\x1ey\\xb9"
                                                                                            "\\x82\\xcb\\x96\\xb1"
                                                                                            "\\xb1\\xde\\xdf\\xe0"
                                                                                            "\\xb2^\\xb4\\xcd\\xb2"
                                                                                            "/\\xfc\\xd4\\xd8Nv5o'",
                                                      'post': 'pop',
                                                      'tests': []})  # пример юзера из DB который идет на вход в класс.
    # на входе поле tests было пустым
    app.exec_()
