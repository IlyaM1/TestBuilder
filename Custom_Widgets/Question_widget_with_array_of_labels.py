from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QWidget
from PyQt5.Qt import pyqtSignal

class Question_widget_with_array_of_labels(QWidget):
    """
    Виджет имеющий question_input, answer_input, ball_input, array_of_labels
    """

    def __init__(self):
        super().__init__()
        self.question_input = None
        self.answer_input = None
        self.ball_input = None
        self.array_of_labels = []
