from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel

class Container(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.expanded = False
        self.setFixedHeight(0)

    def setExpand(self, expanded = False):
        self.expanded = expanded
        if expanded:
            self.setMinimumHeight(0)
            self.setMaximumHeight(0)
        else:
            self.setMinimumHeight(self.sizeHint().height())
            self.setMaximumHeight(16777215)


class CollapsibleBox(QtWidgets.QWidget):
    """
    Раздвигающийся по нажатию виджет
    """
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(text=title, checkable=True, checked=True)
        self.toggle_button.setStyleSheet("QToolButton {background-color:#dadada;}")
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.ArrowType.RightArrow)
        self.toggle_button.released.connect(self.on_pressed)

        self.content_area = Container()

        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        # # self.content_area = QtWidgets.QScrollArea(maximumHeight=0, minimumHeight=0)
        # self.content_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        # self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)
        lay.setAlignment(Qt.AlignTop)

        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation(QtCore.QPropertyAnimation(self.content_area, b"maximumHeight"))

    @QtCore.pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(QtCore.Qt.ArrowType.DownArrow if not checked else QtCore.Qt.ArrowType.RightArrow)
        self.toggle_animation.setDirection(QtCore.QAbstractAnimation.Forward if not checked else QtCore.QAbstractAnimation.Backward)
        self.adjustSize()
        self.content_area.setExpand(checked)
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        collapsed_height = self.sizeHint().height() - self.content_area.maximumHeight()
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(500)
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(self.toggle_animation.animationCount() - 1)
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)

if __name__ == '__main__':
    app = QApplication([])
    w = QMainWindow()
    box_for_wrong_questions = CollapsibleBox(title="Вопросы: ", parent=w)
    box_for_wrong_questions_layout = QVBoxLayout()
    box_for_wrong_questions_layout.addWidget(QLabel("123"))
    box_for_wrong_questions_layout.addWidget(QLabel("1234"))
    box_for_wrong_questions_layout.addWidget(QLabel("1235"))
    box_for_wrong_questions_layout.setAlignment(Qt.AlignTop)
    box_for_wrong_questions.setContentLayout(box_for_wrong_questions_layout)
    w.show()
    app.exec_()