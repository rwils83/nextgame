from .base_config import BaseConfig

class ServerConfig(BaseConfig):
    def __init__(self, config_file):
        super().__init__(config_file)

    def port(self):
        return self.get(["port"])

    def log_level(self):
        return self.get(["logging", "log_level"])

    def log_file(self):
        return self.get(["logging", "log_file"])
