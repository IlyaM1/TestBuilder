from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QMainWindow
from PyQt5.QtCore import Qt
from test_data_funcs import get_all_tests
# from Custom_Widgets.LineEdit_with_explanation import LineEdit_with_explanation
class Admin_test_view(QMainWindow):
    """
        Окошко для изменения и создания теста
        """
    def __init__(self, test={}, parent=None):
        super(QWidget, self).__init__(parent)
        self.test = test
        if self.test == {}:
            self.test = {"name": "", "theme": ""}
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        with open("css/Admin_test_view.css") as css:
            self.setStyleSheet(css.read())
        self.scroll_widget = QScrollArea()
        self.container_widget = QWidget()
        self.container = QVBoxLayout(self)

        self.name_label = QLabel("Имя теста: ")
        self.container.addWidget(self.name_label)

        self.name_input_label = QLineEdit(self.test["name"])
        self.container.addWidget(self.name_input_label)


        self.theme_label = QLabel("Тема теста: ")
        self.container.addWidget(self.theme_label)

        self.theme_input_label = QLineEdit(self.test["theme"])
        self.container.addWidget(self.theme_input_label)

        self.question_label = QLabel("Вопросы: ")
        self.container.addWidget(self.question_label)

        for i in self.test["questions"]:
            self.container.addWidget(self.init_layout_of_question(i))

        self.new_question_button = QPushButton("Добавить вопрос")
        self.new_question_button.released.connect(self.new_question_button_released)
        self.container.addWidget(self.new_question_button)

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

    def init_layout_of_question(self, question):
        self.question_widget = QWidget()

        self.question_layout =  QVBoxLayout()

        self.question_label = QLineEdit(question["question"])
        self.question_layout.addWidget(self.question_label)

        self.variants_of_answer_widget = QWidget()
        self.variants_of_answer_layout = QVBoxLayout()
        for variant in question["variants_of_answer"]:
            variant_of_answer_label = QLineEdit(variant)
            self.variants_of_answer_layout.addWidget(variant_of_answer_label)
        self.variants_of_answer_widget.setLayout(self.variants_of_answer_layout)

        self.question_layout.addWidget(self.variants_of_answer_widget)

        self.question_widget.setLayout(self.question_layout)
        return self.question_widget

    def new_question_button_released(self):
        print("new question")

    def save_button_released(self):
        print("saved")



if __name__ == '__main__':
    app = QApplication([])
    test = get_all_tests()[0]
    for i in range(20):
        test["questions"].append(test["questions"][0])
    auth_obj = Admin_test_view(test)
    # auth_obj = Admin_test_view()

    app.exec_()