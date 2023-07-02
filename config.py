import json


class Config:
    __instance = None

    def __init__(self):
        if Config.__instance is None:
            self.config = open("config.json").read()
            self.config = json.loads(self.config)
        else:
            raise Exception("Config singlton already created")

    @staticmethod
    def get_instance():
        if Config.__instance is None:
            Config.__instance = Config()

        return Config.__instance

    @staticmethod
    def get_path():
        return Config.get_instance().config["path"]
