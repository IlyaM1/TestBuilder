import json


class Config:
    def __init__(self):
        self.config = open("D:\\Programming\\Python\\TestBuilder\\config.json").read()
        self.config = json.loads(self.config)
