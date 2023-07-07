from config import Config
from View.view import View
from PyQt5 import QtWidgets, QtGui, QtCore


class TestEditorViewSignals(QtCore.QObject):
    save_clicked = QtCore.pyqtSignal()


class TestEditorView(View):
    def __init__(self, test=None):
        super().__init__(TestEditorViewSignals())
        if test is None:
            pass

    @staticmethod
    def generate_empty_test():
        return {"id": -1,
                "name": "",
                "theme": "",
                "max_result": 0,
                "questions": []}


if __name__ == '__main__':
    pass
