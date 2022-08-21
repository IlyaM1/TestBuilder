import json


class Config:
    def __init__(self):
        self.config = open("config.json").read()
        self.config = json.loads(self.config)
