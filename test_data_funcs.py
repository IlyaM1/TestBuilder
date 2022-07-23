import random
def get_users(user_login_password=""):
    user = {"name": "Sanya", "id": random.randint(1, 10000)}
    return [user for i in range(5)]

def get_all_tests(user={}):
    # getting all tests of user(completed and not) and returning list of tests
    dictionary = {
        "name": "Тест по анатомии",
        "id": 1,
        "theme": "theme",
        "questions": [
            {
                "question": "question",
                "type": 1,
                "variants_of_answer": ["1", "2", "3", "4"],
                "answer": "2",
                "balls": 1
            },
            {
                "question": "question2",
                "type": 1,
                "variants_of_answer": ["1", "2", "3", "4"],
                "answer": "3",
                "balls": 1
            }
        ]
    }
    testss = [dictionary for i in range(4)]
    return testss