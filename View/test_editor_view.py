from config import Config
from View.view import View
from PyQt5 import QtWidgets, QtGui, QtCore
from Model.entity import Test, Question
from View.ui_utils import UiUtils, HorizontalLabelWithInput


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
            question_widget = self.__generate_one_question_widget(question)
            questions_list_layout.addWidget(question_widget)
        questions_list_widget = UiUtils.generate_widget_with_layout(questions_list_layout)

        add_question_button = UiUtils.generate_button("Добавить вопрос", self.__add_question_button_clicked)
        final_layout = UiUtils.generate_vertical_layout(question_label, questions_list_widget, add_question_button)
        final_widget = UiUtils.generate_widget_with_layout(final_layout)
        scroll_widget = UiUtils.generate_scroll_widget(final_widget)

        return scroll_widget

    @staticmethod
    def __generate_one_question_widget(question: Question) -> QtWidgets.QWidget:
        question_widget = HorizontalLabelWithInput("Вопрос ", question.question)  # TODO: Add deleting question button
        variants_of_answer_widget = TestEditorView.__generate_variants_of_answer_widget(question.variants_of_answer)
        answer_widget = HorizontalLabelWithInput("Ответ ", question.answer)
        points_widget = HorizontalLabelWithInput("Балл ", str(question.points))

        layout = UiUtils.generate_vertical_layout(question_widget,
                                                  variants_of_answer_widget,
                                                  answer_widget,
                                                  points_widget)
        widget = UiUtils.generate_widget_with_layout(layout)
        return widget

    @staticmethod
    def __generate_variants_of_answer_widget(variants_of_answer: list[str]) -> QtWidgets.QWidget:
        label = QtWidgets.QLabel("Варианты ответа")
        layout = UiUtils.generate_vertical_layout(label)
        for variant in variants_of_answer:
            input = QtWidgets.QLineEdit(variant)
            layout.addWidget(input)
        return UiUtils.generate_widget_with_layout(layout)

    def __save_button_clicked(self) -> None:
        self.signals.save_clicked.emit()

    def __add_question_button_clicked(self) -> None:
        pass


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
