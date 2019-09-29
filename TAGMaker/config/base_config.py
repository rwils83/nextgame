import json


class BaseConfig(object):
    def __init__(self, conf_file):
        with open(conf_file, 'r') as conf_file:
            self.data = json.load(conf_file)

    def get(self, key_path):
        result = self.data
        for key in key_path:
            result = result[key]
        return result
