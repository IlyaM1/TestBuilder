# import os
import hashlib
# from sqlite import SQLInteract


def hash_password(password, enc_decode_fmt='utf-8', to_str=True):  # функция хеширования строки
    salt = b'\x89g\xd0\xad\xa4~\x7f\xfc?\xe0\xd6\xb4n\xcd\x90\xc0Q\xdf3\x9bV\xa2(K\n\x03\xae\xf1\xfc\x01\xa9\xd3'
    key = hashlib.pbkdf2_hmac('sha512', password.encode(enc_decode_fmt), salt, iterations=150000)
    if to_str:
        return str(key)
    else:
        return key


# print(hash_password('1213'))

# s = SQLInteract(table_name='socks')
# new_user = [0, "Rel", str(hash_password('1213')), 'as', "[]"]
# s.sql_add_new_user(new_user)
# print(s.return_full_table())
# print(s.sql_get_user_with_namePass('Rel', hash_password('1213')))
# print(1)
# s.drop_table()
# s.sql_create_new_table()

