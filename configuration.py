import configparser

class Configuration:
	def __init__(self, filename):
		self.config = configparser.ConfigParser()
		self.config.read(filename)

		if(not self.config):
			print('Could not open the file {0}'.format(filename))
			return False

		instagram = self.config['INSTAGRAM']


		self.instagram_username = instagram.get('username', None)
		self.instagram_password = instagram.get('password', None)
		print(self.instagram_password)
		