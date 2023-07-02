from enum import Enum
from db.sqlite import SQLInteract
from db.auth_reg import Signing
from config import Config


class LoginStatus(Enum):
    ADMIN = 1
    USER = 2
    EMPTY_FIELDS = 3
    INCORRECT_AUTH_INFO = 4


class AuthInfo:
    def __init__(self, name, password):
        self.name = name
        self.password = password


class AuthorizationModel:
    def __init__(self):
        self.user_db = SQLInteract(table_name='testcase', filename_db=Config.get_path() + '/db/users.db')
        self.test_db = SQLInteract(table_name='tests', filename_db=Config.get_path() + '/db/users.db',
                                   values_of_this_table="(id, name, theme, max_result, questions)")

    def login(self, auth_info: AuthInfo):
        """
        :param auth_info: AuthInfo object with name and password from inputs of auth widget
        :return: Array, where first element LoginStatus and second element is user if LoginStatus==USER
        """

        if auth_info.name == '' or auth_info.password == '':
            return [LoginStatus.EMPTY_FIELDS]

        if auth_info.name == Config.get_instance().config["name"] \
                and auth_info["password"] == self.cfg.config["password"]:
            return [LoginStatus.ADMIN]

        user = self.__authorization(auth_info)
        if user is not False and user is not None:
            return [LoginStatus.USER, user]
        else:
            return [LoginStatus.INCORRECT_AUTH_INFO]

    def __authorization(self, auth_info):
        sign_obj = Signing(auth_info, self.user_db)
        return sign_obj.authentication()
