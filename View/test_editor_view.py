from config import Config
from View.view import View
from PyQt5 import QtWidgets, QtGui, QtCore
from Model.entity import Test, Question
from View.ui_utils import UiUtils, HorizontalLabelWithInput, DeleteButton


class TestEditorViewSignals(QtCore.QObject):
    save_clicked = QtCore.pyqtSignal()


class TestEditorView(View):
    def __init__(self, test: Test = None) -> None:
        super().__init__(TestEditorViewSignals())
        self.test = test
        if test is None:
            self.test = Test()

        self.__set_start_settings()

        constant_widget = self.__generate_constant_widget()
        questions_widget = self.__generate_questions_widget()
        save_button = UiUtils.generate_button("Сохранить", self.__save_button_clicked)

        final_layout = UiUtils.generate_vertical_layout(constant_widget, questions_widget, save_button)
        final_widget = UiUtils.generate_widget_with_layout(final_layout)

        container = QtWidgets.QVBoxLayout(self)
        container.addWidget(final_widget)

    def __set_start_settings(self) -> None:
        self.__set_window_settings()
        self.__set_css()

    def __set_window_settings(self) -> None:
        self.setMinimumSize(1280, 720)
        self.setWindowTitle("Редактор теста")

    def __set_css(self) -> None:
        with open(Config.get_path() + '/View/css/test_editor_view.css') as f:
            self.setStyleSheet(f.read())

    def __generate_constant_widget(self) -> QtWidgets.QWidget:
        self.name_widget = HorizontalLabelWithInput("Имя: ", self.test.name)
        self.theme_widget = HorizontalLabelWithInput("Тема: ", self.test.theme)
        layout = UiUtils.generate_vertical_layout(self.name_widget, self.theme_widget)
        return UiUtils.generate_widget_with_layout(layout)

    def __generate_questions_widget(self) -> QtWidgets.QWidget:
        question_label = QtWidgets.QLabel("Вопросы: ")

        questions_list_layout = QtWidgets.QVBoxLayout()
        for question in self.test.questions:
            self.__add_question(questions_list_layout, question)

        questions_list_widget = UiUtils.generate_widget_with_layout(questions_list_layout)

        add_question_button = QtWidgets.QPushButton("Добавить вопрос")
        add_question_button.clicked.connect(lambda: self.__add_question(questions_list_layout, Question()))

        final_layout = UiUtils.generate_vertical_layout(question_label, questions_list_widget, add_question_button)
        final_widget = UiUtils.generate_widget_with_layout(final_layout)
        scroll_widget = UiUtils.generate_scroll_widget(final_widget)

        return scroll_widget

    def __save_button_clicked(self) -> None:
        self.signals.save_clicked.emit()

    @staticmethod
    def __add_question(layout: QtWidgets.QBoxLayout, question: Question) -> None:
        question_widget = QuestionWidget(question)
        delete_lambda = lambda widget=question_widget: UiUtils.delete_widget_from_layout(layout, widget)
        question_widget.deleting.connect(delete_lambda)
        layout.addWidget(question_widget)


class QuestionWidget(QtWidgets.QWidget):
    deleting = QtCore.pyqtSignal()

    def __init__(self, question: Question, parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent=parent)

        question_widget = HorizontalLabelWithInput("Вопрос ", question.question)  # TODO: Add deleting question button
        delete_question_button = DeleteButton("Вы уверены что хотите удалить этот вопрос?")
        delete_question_button.confirmed.connect(self.__delete_question_clicked)
        question_widget.layout.addWidget(delete_question_button)

        variants_of_answer_widget = self.__generate_variants_of_answer_widget(question.variants_of_answer)
        answer_widget = HorizontalLabelWithInput("Ответ ", question.answer)
        points_widget = HorizontalLabelWithInput("Балл ", str(question.points))

        layout = UiUtils.generate_vertical_layout(question_widget,
                                                  variants_of_answer_widget,
                                                  answer_widget,
                                                  points_widget)
        self.setLayout(layout)

    def __generate_variants_of_answer_widget(self, variants_of_answer: list[str]) -> QtWidgets.QWidget:
        label = QtWidgets.QLabel("Варианты ответа")

        variants_of_answer_layout = QtWidgets.QVBoxLayout()
        for variant_text in variants_of_answer:
            self.__add_variant_widget(variants_of_answer_layout, variant_text)

        add_variant_button = QtWidgets.QPushButton("Добавить вариант ответа")
        add_variant_button.clicked.connect(lambda: self.__add_variant_widget(variants_of_answer_layout))

        layout = UiUtils.generate_vertical_layout(label,
                                                  UiUtils.generate_widget_with_layout(variants_of_answer_layout),
                                                  add_variant_button)
        return UiUtils.generate_widget_with_layout(layout)

    def __delete_question_clicked(self):
        self.deleting.emit()

    def __add_variant_widget(self, layout: QtWidgets.QBoxLayout, text: str = ""):
        variant_widget = self.VariantWidget(text)
        variant_widget.deleting.connect(lambda: UiUtils.delete_widget_from_layout(layout, variant_widget))
        layout.addWidget(variant_widget)

    class VariantWidget(QtWidgets.QWidget):
        deleting = QtCore.pyqtSignal()

        def __init__(self, text: str = ""):
            super().__init__()
            self.input = QtWidgets.QLineEdit(text)
            self.delete_button = DeleteButton("Вы уверены что хотите удалить этот вариант ответа?")
            self.delete_button.confirmed.connect(self.delete_button_clicked)

            self.layout = QtWidgets.QHBoxLayout()
            UiUtils.layout_add_widgets(self.layout, self.input, self.delete_button)
            self.setLayout(self.layout)

        def delete_button_clicked(self):
            self.deleting.emit()


if __name__ == '__main__':
    test = Test(
        1,
        "MyTest",
        "EGE",
        2,
        [
            Question("Govno?", "Yes", 1, ["Yes", "No"]),
            Question("2 + 2", "4", 1, ["1", "4"])
        ]
    )
    app = QtWidgets.QApplication([])
    editor = TestEditorView(test)
    editor.show()
    app.exec()
