from PyQt5.QtWidgets import QLabel, QMenu, QAction
from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import Qt
class Clickable_label(QLabel):
    """
    QLabel на который можно нажать, который хранит в себе dictionary, также имеет контекстное меню из трёх действий: посмотреть детальную информацию(?), изменить, удалить
    """
    clicked = pyqtSignal()

    def __init__(self, text, dictionary):
        super(Clickable_label, self).__init__(text)
        self.dictionary = dictionary

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            super().mouseReleaseEvent(e)
            self.clicked.emit()
