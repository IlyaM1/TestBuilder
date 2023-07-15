from View.test_editor_view import TestEditorView
from View.ui_utils import UiUtils
from Presenter.presenter import Presenter
from Model.entity import Test
from PyQt5 import QtCore


class TestEditorPresenter(Presenter):
    finished = QtCore.pyqtSignal(dict)

    def __init__(self, view: TestEditorView) -> None:
        super().__init__(view)
        self.test = None
        self.view.signals.save_clicked.connect(self.save_test)

    def get_test(self) -> Test:
        try:
            test = self.view.collect_inputs_and_create_test()
        except TypeError:
            UiUtils.call_error_window("Введите в поле балла число")
        else:
            self.test = test
            self.finished.emit(test)
