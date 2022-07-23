import random
def get_users(user_login_password=""):
    users = [{"name": "Sanya", "id": random.randint(1, 10000)} for i in range(5)]

    return users

def get_all_tests(user={}):
    # getting all tests of user(completed and not) and returning list of tests
    testss = [{
        "name": "Тест по анатомии",
        "id": random.randint(1, 10000),
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
    } for i in range(4)]
    return testss