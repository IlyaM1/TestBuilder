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

    def collect_inputs_and_create_test(self) -> Test:
        name = self.name_widget.input.text()
        theme = self.theme_widget.input.text()
        questions = self.__collect_questions()
        max_result = self.__count_max_result(questions)

        return Test(id=self.test.id, name=name, theme=theme, max_result=max_result, questions=questions)

    def __collect_questions(self) -> list[Question]:
        questions: list[Question] = []
        layout = self.questions_list_layout
        for i in range(layout.count()):
            widget: QuestionWidget = layout.itemAt(i).widget()
            question = widget.get_question()
            questions.append(question)

        return questions

    @staticmethod
    def __count_max_result(questions: list[Question]) -> int:
        max_result = 0
        for question in questions:
            max_result += question.points
        return max_result

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

        self.questions_list_layout = QtWidgets.QVBoxLayout()
        for question in self.test.questions:
            self.__add_question(self.questions_list_layout, question)

        questions_list_widget = UiUtils.generate_widget_with_layout(self.questions_list_layout)

        add_question_button = QtWidgets.QPushButton("Добавить вопрос")
        add_question_button.clicked.connect(lambda: self.__add_question(self.questions_list_layout, Question()))

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

        self.question_widget = HorizontalLabelWithInput("Вопрос ",
                                                        question.question)  # TODO: Add deleting question button
        delete_question_button = DeleteButton("Вы уверены что хотите удалить этот вопрос?")
        delete_question_button.confirmed.connect(self.__delete_question_clicked)
        self.question_widget.layout.addWidget(delete_question_button)

        variants_of_answer_widget = self.__generate_variants_of_answer_widget(question.variants_of_answer)
        self.answer_widget = HorizontalLabelWithInput("Ответ ", question.answer)
        self.points_widget = HorizontalLabelWithInput("Балл ", str(question.points))

        layout = UiUtils.generate_vertical_layout(self.question_widget,
                                                  variants_of_answer_widget,
                                                  self.answer_widget,
                                                  self.points_widget)
        self.setLayout(layout)

    def get_question(self) -> Question:
        question = self.question_widget.input.text()
        answer = self.answer_widget.input.text()
        points = self.points_widget.input.text()
        variants_of_answer = self.__collect_variants_of_answer()

        try:
            points = int(points)
        except TypeError:
            raise TypeError("User entered not number in points input")
        else:
            return Question(question=question, answer=answer, points=points, variants_of_answer=variants_of_answer)

    def __collect_variants_of_answer(self) -> list[str]:
        variants_of_answer = []
        for i in range(self.variants_of_answer_layout.count()):
            widget: QuestionWidget.VariantWidget = self.variants_of_answer_layout.itemAt(i).widget()
            text = widget.get_text()
            variants_of_answer.append(text)
        return variants_of_answer

    def __generate_variants_of_answer_widget(self, variants_of_answer: list[str]) -> QtWidgets.QWidget:
        label = QtWidgets.QLabel("Варианты ответа")

        self.variants_of_answer_layout = QtWidgets.QVBoxLayout()
        for variant_text in variants_of_answer:
            self.__add_variant_widget(self.variants_of_answer_layout, variant_text)

        add_variant_button = QtWidgets.QPushButton("Добавить вариант ответа")
        add_variant_button.clicked.connect(lambda: self.__add_variant_widget(self.variants_of_answer_layout))

        layout = UiUtils.generate_vertical_layout(label,
                                                  UiUtils.generate_widget_with_layout(self.variants_of_answer_layout),
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

        def get_text(self):
            return self.input.text()

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
