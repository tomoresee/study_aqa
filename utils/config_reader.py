import yaml


class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config = yaml.safe_load(open("utils/config.yaml"))
        return cls._instance

    @classmethod
    def get(cls, key):
        instance = cls()
        value = instance.config
        for item in key.split("."):
            value = value[item]
        return value
