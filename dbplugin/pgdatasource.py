import postgresql

from dbplugin.exceptions.NotInitializedDataSourceException import NotInitializedDataSourceException
from logger.logger import Logger

""" Data source to postgres database. """
class PGDataSource:
    def __init__(self, username, password, host, database, logger: Logger = None):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.logger = logger

        self.connection = None

    def connect(self):
        if self.username is None or self.password is None or self.host is None or self.database is None:
            return False

        try:
            self.connection = postgresql.open('pq://{0}:{1}@{2}/{3}'.format(self.username, self.password, self.host, self.database))
        except postgresql.exceptions.ClientCannotConnectError:
            return False

        if self.logger is not None:
            self.logger.log('Connected to Postgresql database.')
        return True

    def getConnection(self):
        if self.connection is None:
            raise NotInitializedDataSourceException('Connection was not initialized.')
        return self.connection