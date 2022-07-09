from PyQt5.QtWidgets import  QLabel
from PyQt5.Qt import pyqtSignal

class Item(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text, id):
        super(Item, self).__init__(text)
        self.id = id

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()
