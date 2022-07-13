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
        self.values = self.generating_values()
        self.db_connection = self.sql_connect(self.filename_db)
        self.cursor_obj = sqlite3.Cursor(self.db_connection)

    @staticmethod
    def sql_connect(filename_Db):
        try:
            con = sqlite3.connect(filename_Db)
            return con
        except:
            print(Error)

    def sql_add_new_user(self, user_obj):
        user_obj[0] = self.search_max_int_field() + 1
        self.cursor_obj.execute(
            f'''INSERT INTO {self.table_name}{self.values_of_this_table} VALUES{self.values}''', user_obj)

    def sql_create_new_table(self):
        self.cursor_obj.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} {self.values_of_this_table}")
        self.db_connection.commit()

    def sql_delete_one(self, search_name="id", need_value_of_name="DEfault VaLue123Qwcsa"):
        """real need_value_of_name = f'(SELECT MAX(id) FROM {self.table_name})'"""
        if need_value_of_name == "DEfault VaLue123Qwcsa":
            need_value_of_name = f"(SELECT MAX(id) FROM {self.table_name})"
        self.cursor_obj.execute(f"DELETE FROM {self.table_name} WHERE {search_name}={need_value_of_name}")
        self.db_connection.commit()

    def sql_update_one(self, update_field, update_value,  search_value, search_by='id'):
        """if type update_value == str: update_value must be quotes in quotes "'some text'" """
        self.cursor_obj.execute(f'''UPDATE {self.table_name} SET {update_field} = {update_value} WHERE {search_by} = {search_value}''')

    def sql_free_command(self, command):
        self.cursor_obj.execute(command)

    def return_full_table(self, name_of_table="0"):
        """with no arguments just return table list"""
        if name_of_table == "0":  # если ничего юзер не указал, то выводим всю таблицу указанную при инициализации класса
            name_of_table = self.table_name
        with self.db_connection:
            self.cursor_obj.execute(f"SELECT * FROM {name_of_table}")
            rows = self.cursor_obj.fetchall()
            return rows

    def generating_values(self):  # это в sql такой запар паходу с этим, нужно вельюсы генерить вот так, а потом
        # подставлять в инсерт
        count_comma = self.values_of_this_table.count(",")
        values_str = "(?" + (", ?" * count_comma) + ")"
        return values_str

    def search_max_int_field(self, search_name="id"):  # поиск максимального инт значения в дб
        self.cursor_obj.execute(
            f"SELECT * FROM {self.table_name} WHERE {search_name}=(select max({search_name}) from {self.table_name})")
        max_id = self.cursor_obj.fetchall()
        if len(max_id) == 0:
            return 0
        else:
            return max_id[0][0]


# if __name__ == '__main__':
    # s = SQLInteract()
    # print(s.return_full_table())
    # s.sql_update_one("name", "'Jim'", 2)
    # new_user = [0, "Ilya", "555", "Junior", "[]"]
    # # print(s.generating_values())
    # s.sql_add_new_user(user_obj=new_user)
    # # s.sql_delete_one(need_value_of_name=8)
    # print(s.return_full_table())

