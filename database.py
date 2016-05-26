import postgresql

class DataSource:
	def __init__(self, user, password, host, database_name):
		if (not self or not password or not host or not database_name):
			self.connection = None
		else:
			self.connection = postgresql.open('pq://{0}:{1}@{2}/{3}'.format(user, password, host, database_name))

	def get_data_source(self):
		return self.connection
		
		