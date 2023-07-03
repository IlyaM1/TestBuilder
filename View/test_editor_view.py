from config import Config
from View.view import View
from PyQt5 import QtWidgets, QtGui, QtCore


class TestEditorViewSignals(QtCore.QObject):
    save_clicked = QtCore.pyqtSignal()


class TestEditorView(View):
    def __init__(self):
        super().__init__(TestEditorViewSignals())


if __name__ == '__main__':
    pass
