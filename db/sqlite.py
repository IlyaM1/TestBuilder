import sqlite3
from sqlite3 import Error
import json


class SQLInteract:
    """в values_of_this_table можно использовать только ключевые слова PRIMARY, KEY, UNIQUE.
    заметка на завтра в values_of_this_table указывать что хочешь, а нужную часть для generate_dict() обозначать особыми символами"""

    # в идеале, чтобы вообще все происходило внутри класса (даже коннект и задача курсора),
    # а внизу чисто аргументы писал и все, как проснусь - доделаю, но пока мне нравится
    # по моей задумке для каждой таблицы ты создаешь новый объект класса, и взаимодействуешь с ним в рамках класса
    def __init__(self, filename_db="../db/users.db", table_name="employees",
                 values_of_this_table="(id, name, password, "
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
        self.db_connection.commit()

    def sql_create_new_table(self):
        """После инициализации нужно один раз ручками создать таблицу, ну вот надо так.
        Создается она на основании данных заполненных при инициализации класса"""
        self.cursor_obj.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} {self.values_of_this_table}")
        self.db_connection.commit()

    def sql_delete_one(self, search_name="id", need_value_of_name="DEfault VaLue123Qwcsa"):
        """real need_value_of_name = f'(SELECT MAX(id) FROM {self.table_name})'"""
        if need_value_of_name == "DEfault VaLue123Qwcsa":
            need_value_of_name = f"(SELECT MAX(id) FROM {self.table_name})"
        self.cursor_obj.execute(f"DELETE FROM {self.table_name} WHERE {search_name}={need_value_of_name}")
        self.db_connection.commit()

    def sql_update_one_by_id(self, update_field, update_value, search_id):
        """if type update_value == str: update_value must be quotes in quotes "'some text'" """
        if type(update_value) == str:
            update_value = update_value.replace('"', "'")
            self.cursor_obj.execute(f'''UPDATE {self.table_name} SET {update_field} = "{update_value}"'''
                                    f'''WHERE id = {search_id}''')
        else:
            self.cursor_obj.execute(
                f'''UPDATE {self.table_name} SET {update_field} = {update_value}'''  # разница в кавычках
                f'''WHERE id = {search_id}''')
        self.db_connection.commit()

    def sql_free_command(self, command):
        self.cursor_obj.execute(command)
        self.db_connection.commit()

    def sql_get_user_with_namePass(self, name, password):
        self.cursor_obj.execute(f'''SELECT * FROM {self.table_name} WHERE name = "{name}"'''
                                f''' AND password = "{password}"''')
        row = self.cursor_obj.fetchone()
        dict_row = self.generate_dict(row)
        return dict_row

    def sql_get_user_with_id(self, input_id):
        self.cursor_obj.execute(f'''SELECT * FROM {self.table_name} WHERE id = {input_id}''')
        row = self.cursor_obj.fetchone()
        dict_row = self.generate_dict(row)
        return dict_row

    def return_full_table(self, name_of_table="0", revert=False, to_dict=False) -> list:
        """with no arguments just return table list
        revert will be True or False, if True return sorted on date"""
        if name_of_table == "0":  # если ничего юзер не указал, то выводим всю таблицу указанную при инициализации
            # класса
            name_of_table = self.table_name
        with self.db_connection:
            self.cursor_obj.execute(f"SELECT * FROM {name_of_table}")
            rows = self.cursor_obj.fetchall()
            if to_dict:
                for i in range(len(rows)):
                    rows[i] = self.generate_dict(rows[i])
                    rows[i]["tests"] = self.get_all_tests(rows[i]["id"])
            if revert:
                return rows[::-1]
            else:
                return rows

    def generating_values(self):  # это в sql такой запар паходу с этим, нужно вельюсы генерить вот так, а потом
        # подставлять в инсерт
        count_comma = self.values_of_this_table.count(",")
        values_str = "(?" + (", ?" * count_comma) + ")"
        return values_str

    def search_max_int_field(self, search_name="id"):  # поиск максимального инт значения в дб для создания нового юзера
        self.cursor_obj.execute(
            f"SELECT * FROM {self.table_name} WHERE {search_name}=(select max({search_name}) from {self.table_name})")
        max_id = self.cursor_obj.fetchall()
        if len(max_id) == 0:
            return 0
        else:
            return max_id[0][0]

    def generate_dict(self, user):
        values = self.values_of_this_table[1:-1].replace('PRIMARY KEY', '').replace(', UNIQUE', '').replace('(', '') \
            .replace(')', '').replace(' ', '').split(',')
        dict_of_user = []
        for i in range(len(values)):
            dict_of_user.append([values[i], user[i]])
        dict_of_user = dict(dict_of_user)
        return dict_of_user

    def get_all_tests(self, user_id) -> list:
        """возвращает массив тестов юзера по его id"""
        if 'tests' not in self.values_of_this_table:
            return None
        got_user = self.sql_get_user_with_id(user_id)
        return json.loads(got_user["tests"].replace("'", '"'))


if __name__ == '__main__':
    s = SQLInteract()
    #     s.sql_create_new_table()
    #     user1 = (s.sql_get_user_with_namePass('Jim', '123123'))
    #     print(s.sql_get_user_with_id(3))
    #     # s.sql_delete_one()
    print(s.return_full_table(to_dict=True, revert=True))
#     print(type('s') == str)
#     new_user = [0, "Rel", "123123", "Junior", "[]"]
# user_dict = s.generate_dict(s.sql_get_user_with_namePass('Jim', '123123'))
# print(user_dict)

# s.sql_add_new_user(user_obj=new_user)

# s.sql_update_one_by_id("name", "'Jim'", 3)

# s.sql_delete_one(need_value_of_name=2)
# print(s.return_full_table())
