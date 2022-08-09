from PyQt5.QtWidgets import QLabel, QMenu, QAction
from PyQt5.Qt import pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
class Item(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text, id):
        super(Item, self).__init__(text)
        # self.text = text
        self.id = id

    def contextMenuEvent(self, event):
        menu = QMenu()
        self.see_detail_information_action = menu.addAction(f'Посмотреть детальную информацию')
        self.edit_action = menu.addAction('Редактировать')
        self.delete_action = menu.addAction('Удалить')

        self.see_detail_information_action.triggered.connect(self.see_detail_information)
        self.edit_action.triggered.connect(self.edit)
        self.delete_action.triggered.connect(self.delete)

        res = menu.exec_(event.globalPos())

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            super().mouseReleaseEvent(e)
            self.clicked.emit()
        # self.context_menu.popup()

    def see_detail_information(self):
        print("see_detail_information")

    def edit(self):
        print("edit")

    def delete(self):
        print("delete")
