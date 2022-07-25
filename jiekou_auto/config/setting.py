import os
from datetime import datetime

curren_path = os.path.abspath(__file__)
ori_path = os.path.dirname(os.path.dirname(curren_path))


def config_path():
    return ori_path + os.sep + "config"


def log_path():
    return ori_path + os.sep + "log"


def report_path():
    return ori_path + os.sep + "report"


dbconfig = {"host": "127.0.0.1", "user": "root", "password": "123456", "database": "jiekou","port":3306}

class Dyamic():
    pass




