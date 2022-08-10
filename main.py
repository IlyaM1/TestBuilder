from PyQt5.QtWidgets import QApplication
from Interface.Authorization import Authorization
from db.sqlite import SQLInteract
from auth_reg import Signing

def main():
    app = QApplication([])
    auth_obj = Authorization()
    app.exec_()


if __name__ == '__main__':
    main()
    s = SQLInteract(table_name='testcase', filename_db='db/users.db')
    sign = Signing({'id': 0, 'name': 'ILYA2', 'password': '1234', 'post': 'pop', 'test': '[]'}, s)
    # print(sign.authentication())
    # print(sign.authentication())
    # # s.sql_create_new_table()
    # info = {"id": 1, "name": "ILYA", "password": "1234", "post": "newbye", "tests": "[]"}
    # sign = Signing(info, s)
    # sign.registration()
    # print(s.return_full_table())
