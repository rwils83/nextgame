from TAGMaker.logging.server_logger import ServerLogger

class Logger(object):
    __server = None

    @classmethod
    def get_server(cls):
        if not cls.__server:
            print("making one")
            cls.__server = ServerLogger()
        return cls.__server
