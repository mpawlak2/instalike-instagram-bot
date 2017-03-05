import datetime

from logger.logger import Logger


class CLogger(Logger):
    def log(self, message):
        now = datetime.datetime.now()
        print('[{0}]: {1}'.format(now, message))