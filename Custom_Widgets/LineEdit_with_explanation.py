from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QWidget
from PyQt5.Qt import pyqtSignal

class LineEdit_with_explanation(QWidget):
    """
    Виджет имеющий label и input, label нужен для пояснения input-а
    """
    clicked = pyqtSignal()

    def __init__(self, text_of_label, text_of_input):
        super().__init__()
        self.horizontal_layout = QHBoxLayout()

        self.label = QLabel(text_of_label)
        self.label.setMaximumWidth(100)

        self.line_edit = QLineEdit(text_of_input)

        self.horizontal_layout.addWidget(self.label)
        self.horizontal_layout.insertSpacing(1, 50)
        self.horizontal_layout.addWidget(self.line_edit)

        self.setLayout(self.horizontal_layout)
