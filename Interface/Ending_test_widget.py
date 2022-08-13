from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import QSize, Qt
from test_data_funcs import get_all_tests

class Ending_test_widget(QMainWindow):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        with open('css/Ending_test_widget.css') as css:
            self.css_file = css.read()
            self.setStyleSheet(self.css_file)

        self.show()



if __name__ == '__main__':
    app = QApplication([])
    solve_test = Ending_test_widget()

    app.exec_()

