from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont


class Item(QListWidgetItem):
    def __init__(self, text, id):
        super(Item, self).__init__(text)
        self.id = id
