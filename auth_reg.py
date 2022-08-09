from db.hash import hash_password

inputFromFront = {'id': 0, 'name': 'Egor Lob',
                  'password': '123'}  # к нам приходит инфа с фронта, а мы, имея эту инфу пишем под модуль из визио функции


# типа авторизация и возврат инфы, а потом output подгоним под фронт, главное сам модуль

class Signing:
    def __init__(self, auth_info, SQLInteract_obj):
        self.auth_info = auth_info
        self.name = auth_info["name"]
        self.password = auth_info["password"]
        self.password = hash_password(self.password)
        auth_info["password"] = self.password
        self.s = SQLInteract_obj

    def registration(self):
        """если возвратила False, значит рега не сработала"""
        auth_info_arr = [self.auth_info[x] for x in self.auth_info]
        add_check = self.s.sql_add_new_user(auth_info_arr)
        print(self.s.sql_get_user_with_id(auth_info_arr[0]))
        return add_check

    def authentication(self):
        """если возвратила False, значит такого юзера нету, данные введены неверно"""
        user = self.s.sql_get_user_with_namePass(name=self.name, password=self.password)
        return user
