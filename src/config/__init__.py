from .server_config import ServerConfig

class Config(object):

    @classmethod
    def load_server(cls, conf_file):
        cls.server = ServerConfig(conf_file)
