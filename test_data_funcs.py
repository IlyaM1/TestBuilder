import random
def get_users(user_login_password=""):
    user = {
    "id": 123,
    "name": "Egor Rusnov",
    "password": "QwEwQ7",
    "post": "Junior",
    "tests":
    [
        {
    "name": "eee",
    "theme": "rock",
    "result": 50,
    "max_result": 100,
    "typeOfTest": "0 - без записи (учебка) | 1 - запись (зачет)",
    "date": 15153135,
    "test": [
        {
            "queston": "who",
            "answer": "me",
            "key": "me (правильный ответ)",
            "balls": 1
        }, {
            "queston": "кто такой gir",
            "answer": "ya",
            "key": "notme (правильный ответ)",
            "balls": 0
        }
    ]
},
        {
    "name": "eee",
    "theme": "rock",
    "result": 50,
    "max_result": 100,
    "typeOfTest": "0 - без записи (учебка) | 1 - запись (зачет)",
    "date": 15153135,
    "test": [
        {
            "queston": "who",
            "answer": "me",
            "key": "me (правильный ответ)",
            "balls": 1
        }, {
            "queston": "кто такой gir",
            "answer": "ya",
            "key": "notme (правильный ответ)",
            "balls": 0
        }
    ]
}
    ]
}
    users = []
    for i in range(5):
        users.append(user)
        users[i]["id"] = random.randint(1, 10000)

    return users

def get_all_tests(user={}):
    # getting all tests of user(completed and not) and returning list of tests
    testss = [{
        "name": "Тест по анатомии",
        "id": random.randint(1, 10000),
        "theme": "theme",
        "max_result": 100,
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