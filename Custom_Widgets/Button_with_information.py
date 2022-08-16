from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.Qt import pyqtSignal
class Button_with_information(QPushButton):
    """
    Кнопка которая хранит в себе информацию
    """
    def __init__(self, text, info= ""):
        super(Button_with_information, self).__init__(text)
        self.info = info

if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication([])
        auth_obj = Button_with_information("123", 45)
        auth_obj.show()
        app.exec_()