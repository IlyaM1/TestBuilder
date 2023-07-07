from Presenter.presenter import Presenter
from PyQt5 import QtCore


class TestEditorPresenter(Presenter):
    finished = QtCore.pyqtSignal(dict)

    def __init__(self, view, model):
        super().__init__(view, model)
