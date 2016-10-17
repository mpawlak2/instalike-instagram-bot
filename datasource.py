import postgresql

class DataSource:
    def __init__(self, username, password, host, database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database

        self.connection = None

    def connect(self):
        if self.username is None or self.password is None or self.host is None or self.database is None:
            return False

        try:
            self.connection = postgresql.open('pq://{0}:{1}@{2}/{3}'.format(self.username, self.password, self.host, self.database))
        except postgresql.exceptions.ClientCannotConnectError:
            return False

        return True

    def execute(self, sql_query):
        pass
        # if (self.disabled):
        #     return
        # self.connection.execute(sql_query)

    def prepare_procedure(self, procedure_signature):
        pass
        # if (self.disabled):
        #     return None
        # proc = self.connection.proc(procedure_signature)
        # return proc