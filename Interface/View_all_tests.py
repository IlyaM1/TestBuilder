from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QApplication, QSizePolicy, QListWidget, QMainWindow
from PyQt5.QtCore import QSize
from Interface.Item import Item

class View_all_tests(QWidget):

    def __init__(self, tests, user):
        super().__init__()
        self.tests = tests
        self.user = user
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        self.vertical_layout = QVBoxLayout()

        with open('Interface/View_all_tests.css') as f:
            self.setStyleSheet(f.read())

        for test in self.tests:
            test_row = Item(f'{test["name"]}: {len(test["questions"])} вопроса', test["id"])
            test_row.clicked.connect(self.label_test_pushed)
            self.vertical_layout.addWidget(test_row)

        self.setLayout(self.vertical_layout)
        self.show()

    def label_test_pushed(self):
        self.close()

    def button_login_pushed(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    dictionary = {
  "name": "Тест по анатомии",
  "id": 1,
  "theme": "theme",
  "questions": [
    {
      "question": "question",
      "type": 1,
      "variants_of_answer": ["1", "2", "3", "4"],
      "answer": "2",
      "balls": 1
    },
    {
      "question": "question2",
      "type": 1,
      "variants_of_answer": ["1", "2", "3", "4"],
      "answer": "3",
      "balls": 1
    }
  ]
}
    testss = View_all_tests([dictionary for i in range(5)], [])
    app.exec_()