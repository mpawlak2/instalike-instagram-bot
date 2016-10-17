class DataSource:
    def __init__(self, user, password, host, database):
        self.username = user
        self.password = password
        self.host = host
        self.database = database

        # self.disabled = not use_database
        #
        # if (not self or not password or not host or not database_name or self.disabled):
        #     self.connection = None
        # else:
        #     try:
        #         self.connection = postgresql.open('pq://{0}:{1}@{2}/{3}'.format(user, password, host, database_name))
        #     except postgresql.exceptions.ClientCannotConnectError:
        #         print('Error while connecting to database - database disabled.')
        #         self.disabled = True

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