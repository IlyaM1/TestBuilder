from PyQt5 import QtWidgets, QtCore, QtGui
from config import Config


class UiUtils:
    @staticmethod
    def delete_widget_from_layout(layout: QtWidgets.QBoxLayout, sender: QtWidgets.QWidget):
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget == sender:
                layout.removeWidget(widget)
                widget.deleteLater()
                return

    @staticmethod
    def generate_vertical_layout(*widgets: QtWidgets.QWidget):
        layout = QtWidgets.QVBoxLayout()
        UiUtils.layout_add_widgets(layout, *widgets)
        return layout

    @staticmethod
    def layout_add_widgets(layout: QtWidgets.QLayout, *widgets: QtWidgets.QWidget):
        for widget in widgets:
            layout.addWidget(widget)

    @staticmethod
    def generate_widget_with_layout(layout: QtWidgets.QLayout):
        wrapper_widget = QtWidgets.QWidget()
        wrapper_widget.setLayout(layout)
        return wrapper_widget

    @staticmethod
    def generate_wrapper_widget(widget: QtWidgets.QWidget):
        wrapper_widget = QtWidgets.QWidget()
        wrapper_widget.setLayout(UiUtils.generate_vertical_layout(widget))
        return wrapper_widget

    @staticmethod
    def generate_scroll_widget(widget_to_set: QtWidgets.QWidget):
        scroll_widget = QtWidgets.QScrollArea()

        scroll_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_widget.setWidgetResizable(True)
        scroll_widget.setWidget(widget_to_set)

        return scroll_widget

    @staticmethod
    def generate_button(text: str, connect_function, position: QtCore.QPoint = None, width: int = None):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(connect_function)
        if position is not None:
            button.move(position)
        if width is not None:
            button.setMinimumWidth(width)

        return button

    @staticmethod
    def generate_input_label(placeholder_text: str, object_name: str = None):
        input_label_login = QtWidgets.QLineEdit()
        input_label_login.setPlaceholderText(placeholder_text)
        input_label_login.setObjectName(object_name)
        input_label_login.setMaximumWidth(1000)

        return input_label_login

    @staticmethod
    def call_error_window(text: str):
        error_window = QtWidgets.QMessageBox()
        error_window.setText(text)
        error_window.setWindowTitle("Ошибка")
        error_window.exec()


class HorizontalLabelWithInput(QtWidgets.QWidget):
    def __init__(self, label_text: str = "", input_text: str = "", parent=None):
        super().__init__(parent=parent)
        self.label = QtWidgets.QLabel(label_text)
        self.input = QtWidgets.QLineEdit(input_text)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.setLayout(self.layout)


class DeleteButton(QtWidgets.QPushButton):
    confirmed = QtCore.pyqtSignal()

    def __init__(self, confirmation_text: str = "Вы уверены?", parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent)
        self.confirmation_text = confirmation_text
        self.__set_icon()
        self.clicked.connect(self.button_clicked)

    def button_clicked(self) -> None:
        confirmation = QtWidgets.QMessageBox.question(self, "Confirmation", self.confirmation_text,
                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirmation == QtWidgets.QMessageBox.Yes:
            self.confirmed.emit()

    def __set_icon(self) -> None:
        icon_position = Config.get_path() + '\\View\\img\\delete_button.png'
        self.setIcon(QtGui.QIcon(icon_position))
        self.setIconSize(QtCore.QSize(self.sizeHint()))
