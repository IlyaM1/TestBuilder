def get_all_tests(user):
    print("some_magic")
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
    testss = [dictionary for i in range(5)]
    return testss