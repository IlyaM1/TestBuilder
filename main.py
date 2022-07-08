# import PyQt5
from types import SimpleNamespace
from os import remove
import sys
import json

f = open('schemes/user.json')
s = f.read()
jsonn = (json.loads(s))
jsonn["NS"] = '23'
print(jsonn["NS"])
with open("schemes/out.json", "w") as wri:
    print(json.dumps(jsonn))
    wri = json.dumps(jsonn)

data = s

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x.name)

ls = "{'NS': 'JJ', 'id': 228, 'login': 'avg_Master'}"
last = open("schemes/out.json")
sa = last.read()
# print(sa, json.loads(ls))

# with open("out.json", "w") as wri:
#     json.dump(jsonn, wri)
#     # ss = json.load(wri)
#     # remove(wri)

# f2 = open('out.json')
# ff = json.load(f2)
# f2.close()
# # remove('out.json')
# print(str(ff))

if __name__ == '__main__':
    print(5)





