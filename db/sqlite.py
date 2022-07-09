import sqlite3
from sqlite3 import Error


class SQLInteract:  # в идеале, чтобы вообще все происходило внутри класса (даже коннект и задача курсора),
    # а внизу чисто аргументы писал и все, как проснусь - доделаю, но пока мне нравится
    # по моей задумке для каждой таблицы ты создаешь новый объект класса, и взаимодействуешь с ним в рамках класса
    def __init__(self, filename_db="users.db", table_name="employees", values_of_this_table="(id, name, password, "
                                                                                            "post, tests)"):
        self.filename_db = filename_db
        self.table_name = table_name
        self.values_of_this_table = values_of_this_table

    @staticmethod
    def sql_connect(filename_Db):
        try:
            con = sqlite3.connect(filename_Db)
            return con
        except:
            print(Error)

    def sql_add_new_user(self, user_obj):
        user_obj[0] = self.search_max_int_field() + 1
        cursor_obj.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} {self.values_of_this_table}")
        cursor_obj.execute(
            f'''INSERT INTO {self.table_name}{self.values_of_this_table} VALUES{self.generating_values()}''', user_obj)

    def print_full_table(self, name_of_table=0):
        if name_of_table == 0:  # если ничего юзер не указал, то выводим всю таблицу указанную при инициализации класса
            name_of_table = self.table_name
        with db_con:
            cursor_obj.execute(f"SELECT * FROM {name_of_table}")
            rows = cursor_obj.fetchall()
            for row in rows:
                print(row)

    def generating_values(self):  # это в sql такой запар с этим, нужно вельюсы генерить вот так, а потом подставлять
        # в инсерт
        count_comma = self.values_of_this_table.count(",")
        values_str = "(?" + (", ?" * count_comma) + ")"
        return values_str

    def search_max_int_field(self, search_name="id"):  # поиск максимального инт значения в дб
        cursor_obj.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} {self.values_of_this_table}")
        cursor_obj.execute(f"SELECT * FROM {self.table_name} WHERE {search_name}=(select max({search_name}) from {self.table_name})")
        max_id = cursor_obj.fetchall()
        if len(max_id) == 0:
            return 0
        else:
            return max_id[0][0]



if __name__ == '__main__':
    user_db_address = 'users.db'
    s = SQLInteract()
    db_con = s.sql_connect(filename_Db=user_db_address)
    cursor_obj = sqlite3.Cursor(db_con)

    new_user = [1, "Ilya", "555", "Junior", "[]"]
    # print(s.generating_values())
    s.sql_add_new_user(user_obj=new_user)
    s.print_full_table()

    db_con.commit()
