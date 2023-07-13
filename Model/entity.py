from enum import Enum


class EntityType(Enum):
    USER = 1
    TEST = 2


class Entity:
    def __init__(self, id: int, name: str, type: EntityType):
        self.id = id
        self.name = name
        self.type = type


class Question:
    def __init__(self, question: str = "", answer: str = "", points: int = 1, variants_of_answer: list[str] = []):
        self.question = question
        self.answer = answer
        self.points = points
        self.variants_of_answer = variants_of_answer


class Test(Entity):
    def __init__(self, id: int = 0, name: str = "", theme: str = "", max_result: int = 0,
                 questions: list[Question] = []):
        super().__init__(id=id, name=name, type=EntityType.TEST)
        self.theme = theme
        self.max_result = max_result
        self.questions = questions


class SolvedTest:
    pass


class User(Entity):
    def __init__(self, id: int = 0, name: str = "", password: str = "", post: str = "",
                 solved_tests: list[SolvedTest] = []):
        super().__init__(id=id, name=name, type=EntityType.USER)
        self.password = password
        self.post = post
        self.solved_tests = solved_tests
