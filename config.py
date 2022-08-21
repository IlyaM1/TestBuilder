import json


class Config:
    def __init__(self):
        self.config = open("S:/Programming/Python/TestBuilder_main/config.json").read()
        self.config = json.loads(self.config)
