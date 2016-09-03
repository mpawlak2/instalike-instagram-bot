import datetime

class FileOutput:
	def __init__(self, filename, log_db_operations):
		if log_db_operations:
			self.target = open(filename, 'wb')
		else:
			self.target = None

	def close():
		self.target.close()

	def log(self, text):
		if (not self.target):
			return
		action_date = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
		action_text = '{0} -> {1}\n\n'.format(action_date, text)
		try:
			self.target.write(action_text.encode('utf-8'))
		except IOError:
			print('Could not log operation to file.')

		
