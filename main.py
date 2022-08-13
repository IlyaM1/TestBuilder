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
    sign = Signing({'id': 0, 'name': 'ILYA3224', 'password': '1234', 'post': 'pop', 'test': '[]'}, s)
    # print(sign.authentication())
    # print(sign.authentication())
    # # s.sql_create_new_table()
    # info = {"id": 1, "name": "ILYA", "password": "1234", "post": "newbye", "tests": "[]"}

    # print(sign.authentication())
    # print(s.return_full_table())
    # print(s.sql_get_user_with_id(2))
    # print(type(s.get_all_tests(2)))
    # print(s.all_tables_name())

