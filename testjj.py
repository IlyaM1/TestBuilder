import json


def foo(newUser):
    newUser = json.loads(newUser)
    # newUser["name"] = 'No'  # типа поработали с объедком
    # print((newUser))
    # вопрос: в каком виде сохранять строку в дб чтобы ее можно было потом считать? "" или ''
    db = str(json.dumps(newUser, ensure_ascii=False, separators=(',', ':')))  # типа сохранили
    # print((db))
    newUser = (db)  # чтение из дб
    newUser = json.loads(newUser)  # кастим в dict
    print((newUser["name"]))  # вуаля, мы можем опять читать и записывать


newUser = open("schemes/userRdyTest.json", "r", encoding="utf-8").read()  # нам нужон новый юзер на основании этой схемы(
# примера)

# foo(newUser)

newestUser = open("schemes/user.json", "r", encoding="utf-8").read()
foo(newestUser)

