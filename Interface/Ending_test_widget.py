from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QProgressBar
from config import Config as cfg


class Ending_test_widget(QWidget):
    def __init__(self, result=0, wrong_answers=0, max_result=0, user={}, parent=None):
        super(QWidget, self).__init__(parent)
        self.result = result
        self.wrong_answers = wrong_answers
        self.max_result = max_result
        self.user = user
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(400, 300)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Create a horizontal layout for the result labels
        result_layout = QHBoxLayout()
        self.main_layout.addLayout(result_layout)

        # Create a label for the test result
        self.result_label = QLabel(f"Result: {self.result}/{self.max_result}")
        result_layout.addWidget(self.result_label)

        # Create a progress bar to visualize the result
        self.result_progress = QProgressBar()
        self.result_progress.setValue(int((self.result / self.max_result) * 100))
        result_layout.addWidget(self.result_progress)

        # Create a button to close the widget
        self.finish_test_button = QPushButton("Close")
        self.finish_test_button.clicked.connect(self.close)
        self.main_layout.addWidget(self.finish_test_button)

        with open(cfg().config["path"] + '/Interface/css/Ending_test_widget.css', "r") as css:
            self.setStyleSheet(css.read())

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    test_widget = Ending_test_widget(result=5, wrong_answers=7, max_result=12)
    app.exec_()
