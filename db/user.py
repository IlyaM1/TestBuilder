import json
# from db.sqlite import SQLInteract
# from config import Config


# print(db.return_full_table())

def new_user(info_from_front) -> dict:  # not using
    """берем кароч схему юзера из жсона, и записываем туда дату с фронта при создании нового юзверя каста это все в
    словарь"""
    scheme_of_user = open('../schemes/user.json', 'r', encoding='utf-8').read()
    scheme_of_user = json.loads(scheme_of_user)
    # магия записи с фронта и ретерним словарик, теперь можно поработать с новым юзером, только инфа с фронта нужна
    #
    return scheme_of_user


def from_dict_to_str(input_dict: dict) -> str:
    """просто кастим словарь в строку для дальнейшего сохранения в базу"""
    return str(json.dumps(input_dict, ensure_ascii=False, separators=(',', ':')))


def from_str_to_dict(input_str: str) -> dict:
    """просто запись обратно из строки в словарик"""
    return json.loads(input_str)


# if __name__ == '__main__':
#     cfg = Config()
#     db = SQLInteract(filename_db=cfg.config["path"] + "/db/users.db")
#     aaa = '[{"name":"EGE RUSS","rezult":999},{"name":"EGE MATH","rezult":80}]'
#     db.sql_update_one_by_id(update_field="tests", update_value=aaa, search_id=3)
# print(db.return_full_table())
# print(from_str_to_dict(from_dict_to_str(new_user(0))))
# print((get_all_tests(3)))
