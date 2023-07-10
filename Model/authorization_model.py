from enum import Enum
from db.sqlite import SQLInteract
from db.auth_reg import Signing
from config import Config
# from Model.entity import User, Test, Entity, EntityType


class LoginStatus(Enum):
    ADMIN = 1
    USER = 2


class AuthInfo:
    def __init__(self, name: str, password: str):
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
        :return: returns LoginStatus: Admin or User
        """
        if auth_info.name == '' or auth_info.password == '':
            raise EmptyFieldLoginException()
        elif self.__compare_auth_info_with_admin(auth_info):
            return LoginStatus.ADMIN
        else:
            # For person who will make authorization:
            # Error return codes should be replaced with exception
            # And there are shouldn't be "is not None" check, not sure about "is not False"
            user = self.__authorization(auth_info)
            if user is not False and user is not None:
                return LoginStatus.USER
            else:
                raise IncorrectAuthInfoLoginException()

    def get_user_by_auth_info(self, auth_info: AuthInfo):
        """
        Get user from database
        :return: User object
        """
        pass

    def __authorization(self, auth_info: AuthInfo):
        sign_obj = Signing(auth_info, self.user_db)
        return sign_obj.authentication()

    def get_users(self):
        """
        Get all users rows from database and convert to objects
        :return: list of user's objects
        """
        pass

    def get_tests(self):
        """
        Get all tests rows from database and convert to objects
        :return: list of test's objects
        """
        pass

    @staticmethod
    def __compare_auth_info_with_admin(auth_info: AuthInfo):
        is_name_equal = auth_info.name == Config.get_instance().config["name"]
        is_password_equal = auth_info.password == Config.get_instance().config["password"]
        return is_name_equal and is_password_equal


class EmptyFieldLoginException(Exception):
    def __init__(self):
        super().__init__("Login is unsuccessful, because login and/or password inputs are empty")


class IncorrectAuthInfoLoginException(Exception):
    def __init__(self):
        super().__init__("Login is unsuccessful, because login and/or password for admin/user are incorrect")
