class FileOutput:
	def __init__(self, filename):
		self.target = open(filename, 'wb')

	def close():
		self.target.close()

	def log(self, text):
		self.target.write(text)
		