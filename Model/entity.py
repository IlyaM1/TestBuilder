from enum import Enum


class EntityType(Enum):
    USER = 1
    TEST = 2


class Entity:
    def __init__(self, id: int, name: str, type: EntityType):
        self.id = id
        self.name = name
        self.type = type


class User(Entity):
    def __init__(self, id: int = 0, name: str = "", password: str = "", post: str = "", tests: list = []):
        super().__init__(id=id, name=name, type=EntityType.USER)
        self.password = password
        self.post = post
        self.tests = tests


class Test(Entity):
    def __init__(self, id: int = 0, name: str = "", theme: str = "", max_result: int = 0, questions: list = []):
        super().__init__(id=id, name=name, type=EntityType.TEST)
        self.theme = theme
        self.max_result = max_result
        self.questions = questions
