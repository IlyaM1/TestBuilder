from PyQt5.QtWidgets import QApplication
from Interface.Authorization import Authorization

def main():
    app = QApplication([])
    auth_obj = Authorization()
    app.exec_()

if __name__ == '__main__':
    main()