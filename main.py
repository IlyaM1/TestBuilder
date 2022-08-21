from PyQt5.QtWidgets import QApplication
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
    cfg = Config()
    s = SQLInteract(table_name='testcase', filename_db=cfg.config["path"] + '/db/users.db')
    sign = Signing({'id': 0, 'name': '1', 'password': '123', 'post': 'pop', 'tests': '[]'}, s)
    print(cfg.config)
    print(s.return_full_table(to_dict=True))
    # print(sign.authentication())
    # print(sign.authentication())
    # # s.sql_create_new_table()
    # info = {"id": 1, "name": "ILYA", "password": "1234", "post": "newbye", "tests": "[]"}
    # print(sign.authentication())
    # print(s.sql_get_user_with_id(2))
    # print(type(s.get_all_tests(2)))
    # print(s.all_tables_name())
