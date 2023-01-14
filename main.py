from PyQt5.QtWidgets import QApplication, QMainWindow
from Interface.Authorization import Authorization
from db.sqlite import SQLInteract
from auth_reg import Signing
from config import Config

def main():
    app = QApplication([])
    auth_obj = Authorization()
    app.exec_()


if __name__ == '__main__':
    main()
    # sd
    # cfg = Config()
    # print(sign.authentication())
    # print(sign.authentication())
    # # s.sql_create_new_table()
    # info = {"id": 150, "name": "ILYA", "password": "1234", "post": "newbye", "tests": "[]"}
    # s.sql_add_new_user(info)
    # print(sign.authentication())
    # print(s.sql_get_user_with_id(2))
    # print(type(s.get_all_tests(2)))
    # print(s.all_tables_name())

# venv\Scripts\activate