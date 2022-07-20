from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QVBoxLayout


class Admin_view_tests_and_users(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.init_UI()

    def init_UI(self):
        self.setMinimumSize(1280, 720)

        self.container = QVBoxLayout(self)

        self.tab_widget = QTabWidget()

        self.user_page = self.init_users_page()
        self.test_page = self.init_tests_page()

        self.tab_widget.addTab(self.test_page, "Тесты")
        self.tab_widget.addTab(self.user_page, "Сотрудники")

        self.container.addWidget(self.tab_widget)
        self.show()



    def init_users_page(self):
        return QWidget()

    def init_tests_page(self):
        return QWidget()


if __name__ == '__main__':
    app = QApplication([])
    auth_obj = Admin_view_tests_and_users()
    app.exec_()