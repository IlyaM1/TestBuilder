from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QLineEdit
from test_data_funcs import get_all_tests

class Admin_test_view(QWidget):

    def __init__(self, test={}, parent=None):
        super(QWidget, self).__init__(parent)
        self.test = test
        if self.test == {}:
            self.test = {"name": "", "theme": ""}
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        self.container = QVBoxLayout(self)

        self.name_label = QLabel("Имя теста: ")
        self.container.addWidget(self.name_label)

        self.name_input_label = QLineEdit(self.test["name"])
        self.container.addWidget(self.name_input_label)


        self.theme_label = QLabel("Тема теста: ")
        self.container.addWidget(self.theme_label)

        self.theme_input_label = QLineEdit(self.test["theme"])
        self.container.addWidget(self.theme_input_label)

        for i in self.test["questions"]:
            self.container.addWidget(self.init_layout_of_question(i))

        self.container.addWidget(self)
        self.setLayout(self.container) # test thing
        self.show()

    def init_layout_of_question(self, question):
        self.question_layout =  QVBoxLayout()

        self.question_label = QLineEdit(question["question"])
        self.question_layout.addWidget(self.question_label)

        self.variants_of_answer_layout = QVBoxLayout()
        for variant in question["variants_of_answer"]:
            variant_of_answer_label = QLineEdit(variant)
            self.variants_of_answer_layout.addWidget(variant_of_answer_label)

        self.question_layout.addWidget(self.variants_of_answer_layout)

        return self.question_layout




if __name__ == '__main__':
    app = QApplication([])
    test = get_all_tests()[0]
    auth_obj = Admin_test_view(test)
    # auth_obj = Admin_test_view()

    app.exec_()