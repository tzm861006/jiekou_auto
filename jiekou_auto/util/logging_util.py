import logging
from config.setting import log_path
import datetime
import os


class logging_util:
    def __init__(self, consle_stream=True):
        self.logger = logging.getLogger("test")
        self.logger.setLevel(logging.DEBUG)
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d")
        self.handler = logging.FileHandler(log_path() + os.sep + self.current_time, mode="w",
                                           encoding="utf-8")
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)
        if consle_stream:
            self.consle_stream = logging.StreamHandler()
            self.consle_stream.setFormatter(self.formatter)
            self.consle_stream.setLevel(logging.DEBUG)
            self.logger.addHandler(self.consle_stream)

    def get_logger(self):
        return self.logger


logger = logging_util().get_logger()

