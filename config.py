import json
import sys


class Config:
    __instance = None

    def __init__(self):
        if Config.__instance is None:
            self.config = open(Config.get_config_path(sys.argv[0])).read()
            self.config = json.loads(self.config)
        else:
            raise Exception("Config instance already created")

    @staticmethod
    def get_instance():
        if Config.__instance is None:
            Config.__instance = Config()

        return Config.__instance

    @staticmethod
    def get_path():
        return Config.get_instance().config["path"]

    @staticmethod
    def get_config_path(file_path):
        index = file_path.rfind("TestBuilder")
        file_path = file_path[:index + 11]  # +11 для учета длины "TestBuilder"
        config_path = file_path + "\\config.json"
        return config_path
