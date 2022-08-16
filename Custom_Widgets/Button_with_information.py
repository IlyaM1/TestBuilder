from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.Qt import pyqtSignal
class Button_with_information(QPushButton):
    """
    QLabel на который можно нажать, который хранит в себе id объекта для которого создан, также имеет контекстное меню из трёх действий: посмотреть детальную информацию(?), изменить, удалить
    """
    # clicked = pyqtSignal()

    def __init__(self, text, info= ""):
        super(Button_with_information, self).__init__(text)
        self.info = info

    # def mouseReleaseEvent(self):
    #     super().mouseReleaseEvent()
    #     self.clicked.emit()
    #     # self.context_menu.popup()

if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication([])
        auth_obj = Button_with_information("123", 45)
        auth_obj.show()
        app.exec_()