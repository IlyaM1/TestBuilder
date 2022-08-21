from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QWidget, QApplication, QPushButton
from PyQt5.Qt import pyqtSignal
from PyQt5.QtGui import QIcon
from config import Config
class Deletable_LineEdit_with_explanation(QWidget):
    """
    Виджет имеющий label ,и input ,и кнопка-значок, label нужен для пояснения input-а
    """
    clicked = pyqtSignal()

    def __init__(self, text_of_label, text_of_input, path):
        super().__init__()
        self.horizontal_layout = QHBoxLayout()

        self.label = QLabel(text_of_label)
        self.label.setMaximumWidth(100)

        self.line_edit = QLineEdit(text_of_input)

        delete_icon = QIcon(path)
        self.delete_button = QPushButton(icon=delete_icon, text="")
        self.delete_button.setStyleSheet("QPushButton{border:none;background-color:rgba(255, 255, 255,100);}")

        self.horizontal_layout.addWidget(self.label)
        self.horizontal_layout.insertSpacing(1, 50)
        self.horizontal_layout.addWidget(self.line_edit)
        self.horizontal_layout.addWidget(self.delete_button)

        self.setLayout(self.horizontal_layout)

if __name__ == '__main__':
    app = QApplication([])
    auth_obj = Deletable_LineEdit_with_explanation("123", "12", Config().config["path"] + "\\Interface\\Trash_Bin.png")
    auth_obj.show()
    app.exec_()