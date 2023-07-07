from config import Config
from View.view import View
from PyQt5 import QtWidgets, QtGui, QtCore
from Model.entity import Test


class TestEditorViewSignals(QtCore.QObject):
    save_clicked = QtCore.pyqtSignal()


class TestEditorView(View):
    def __init__(self, test: Test = None):
        super().__init__(TestEditorViewSignals())
        self.test = test
        if test is None:
            self.test = Test()


if __name__ == '__main__':
    pass
