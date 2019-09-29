from .base_config import BaseConfig

class ServerConfig(BaseConfig):
    def __init__(self, config_file):
        super().__init__(config_file)

    def port(self):
        return self.get(["port"])
