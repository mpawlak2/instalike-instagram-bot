import datetime

from logger.logger import Logger


class CLogger(Logger):
    def log(self, message):
        now = datetime.datetime.today()
        print('[{0}]: {1}'.format(now.strftime('%Y-%m-%d %H:%M:%S'), message))