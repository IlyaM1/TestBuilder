from PyQt5 import QtWidgets


class View(QtWidgets.QWidget):
    def __init__(self, signals, parent=None):
        super().__init__(parent)
        self.signals = signals
