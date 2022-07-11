from PyQt5.QtWidgets import QApplication
from Interface.Authorization import Authorization
# from Interface.View_all_tests import View_all_tests

def main():
    app = QApplication([])
    auth_obj = Authorization()
    # auth_obj.show()
    # view_all_tests = View_all_tests({}, [])
    app.exec_()

if __name__ == '__main__':
    main()