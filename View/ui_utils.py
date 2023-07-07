from PyQt5 import QtWidgets, QtCore


class UiUtils:
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
    def create_wrapper_widget(layout: QtWidgets.QLayout):
        wrapper_widget = QtWidgets.QWidget()
        wrapper_widget.setLayout(layout)
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
    def generate_button(text: str, connect_function, position: QtCore.QPoint = None, width: int = 300):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(connect_function)
        button.setMinimumWidth(width)
        button.move(position)

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
