from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize, Qt
from test_data_funcs import get_all_tests, get_users
from config import Config

class Ending_test_widget(QMainWindow):
    """
    Окно, которое вызывается после завершения теста
    """
    def __init__(self, result = 0, wrong_answers = 0, max_result = 0, parent=None):
        super(QWidget, self).__init__(parent)
        self.result = result
        self.wrong_answers = wrong_answers
        self.max_result = max_result
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        with open(Config().config["path"] + '\\Interface\\css\\Ending_test_widget.css') as css:
            self.css_file = css.read()
            self.setStyleSheet(self.css_file)

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()

        self.test_finished_label = QLabel("Вы закончили тест")
        self.main_layout.addWidget(self.test_finished_label)

        self.result_label = QLabel(f"Ваш результат: {self.result}/{self.max_result}")
        self.main_layout.addWidget(self.result_label)

        self.wrong_answers_label = QLabel(f"Количество неверно решённых заданий: {self.wrong_answers}")
        self.main_layout.addWidget(self.wrong_answers_label)

        self.finish_test_button = QPushButton("Вернуться к выбору теста")
        self.finish_test_button.released.connect(self.finish_test_button_pushed)
        self.main_layout.addWidget(self.finish_test_button)



        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.show()


    def finish_test_button_pushed(self):
        pass
        # self.close()
        # user = get_users()[0]
        # test = get_all_tests(user)[0]
        # tests = [test for i in range(20)]
        # self.view_all_tests = View_all_tests(tests, user)



if __name__ == '__main__':
    app = QApplication([])
    solve_test = Ending_test_widget()

    app.exec_()

