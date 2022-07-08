import sqlite3
from sqlite3 import Error


def sql_connect(filenameDb):
    try:
        con = sqlite3.connect(filenameDb)
        return con
    except:
        print(Error)


def sql_add_new_user(userObj):
    cursorObj.execute('''INSERT INTO employees VALUES(id, name, password, post, tests) VALUES(?, ?, ?, ?, ?)''',
                      userObj)


userDb = 'users.db'
dbCon = sql_connect(userDb)
cursorObj = sqlite3.Cursor(dbCon)

dbCon.commit()
