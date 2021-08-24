import logging

from TAGMaker.config import Config


class ServerLogger(object):

    __log_format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    __log_level_strmap = {
            "CRITICAL": logging.CRITICAL,
            "ERROR": logging.ERROR,
            "WARNING": logging.WARNING,
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG
            }

    def __init__(self):
        self.logger = logging.getLogger("TAGMaker.Server")
        
        self.logger.setLevel(self.__log_level_strmap.get(Config.server.log_level(), logging.NOTSET))
        file_handler = logging.FileHandler(Config.server.log_file())
        file_formatter = logging.Formatter(self.__log_format_string)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def flush(self):
        self.logger.flush()

    def critical(self, msg):
        self.logger.critical(msg)

    def error(self, msg):
        self.logger.error(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)



