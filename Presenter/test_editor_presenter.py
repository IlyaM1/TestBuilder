from Presenter.presenter import Presenter
from View.admin_panel_view import EntityType
from PyQt5 import QtCore


class TestEditorPresenter(Presenter):
    finished = QtCore.pyqtSignal(dict)

    def __init__(self, view, model):
        super().__init__(view, model)
