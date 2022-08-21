from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication, QHBoxLayout
from PyQt5.QtGui import QIcon
from config import Config
class Deletable_TextInput(QWidget):
    """
    Виджет состоящий из текстового поля и кнопки удаления
    """

    def __init__(self, text, path=Config().config["path"] + "\\Interface\\Trash_Bin.png"):
        super(Deletable_TextInput, self).__init__()

        delete_icon = QIcon(path)
        # delete_icon = QIcon("D:\IT\TestBuilder\Interface\Trash_Bin.png")
        self.text_input = QLineEdit(text)
        self.delete_button = QPushButton(icon=delete_icon, text="")
        self.delete_button.setStyleSheet("QPushButton{border:none;background-color:rgba(255, 255, 255,100);}")

        self.vertical_layout = QHBoxLayout()
        self.vertical_layout.addWidget(self.text_input)
        self.vertical_layout.addWidget(self.delete_button)

        self.setLayout(self.vertical_layout)



if __name__ == '__main__':
    app = QApplication([])
    auth_obj = Deletable_TextInput("123")
    auth_obj.show()
    app.exec_()
