from db.hash import hash_password


inputFromFront = {'name': 'Egor Lob',
                  'password': '123'}  # к нам приходит инфа с фронта, а мы, имея эту инфу пишем под модуль из визио функции


# типа авторизация и возврат инфы, а потом output подгоним под фронт, главное сам модуль

class Signing:
    def __init__(self, auth_info, SQLInteract_obj):
        self.auth_info = auth_info
        self.name = auth_info["name"]
        self.password = auth_info["password"]
        self.password = hash_password(self.password)
        self.s = SQLInteract_obj

    def registration(self):
        auth_info_arr = [self.auth_info[x] for x in self.auth_info]
        self.s.sql_add_new_user(auth_info_arr)
        print(self.s.sql_get_user_with_id(auth_info_arr[0]))

