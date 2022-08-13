from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QWidget


class LineEdit_with_explanation(QWidget):
    clicked = pyqtSignal()

    def __init__(self, text_of_label, text_of_input):
        super().__init__()
        # self.text = text
        self.horizontal_layout = QHBoxLayout()

        self.label = QLabel(text_of_label)
        self.label.setMaximumWidth(100)

        self.line_edit = QLineEdit(text_of_input)

        self.horizontal_layout.addWidget(self.label)
        self.insertSpacing(1, 50)
        self.horizontal_layout.addWidget(self.line_edit)

        self.setLayout(self.horizontal_layout)
