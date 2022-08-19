import json


class Config:
    def __init__(self):
        self.config = open("D:/Documents/Git/TestBuilder/config.json").read()
        self.config = json.loads(self.config)
