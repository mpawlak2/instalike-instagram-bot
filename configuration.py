import configparser

class Configuration:
	def __init__(self, filename):
		self.config = configparser.ConfigParser()
		self.config.read(filename)

		if(not self.config):
			print('Could not open the file {0}'.format(filename))
			return False

		instagram = self.config['INSTAGRAM']
		bot = self.config['BOT']

		# BOT SECTION
		self.bot_work_hours = bot.get('workhoursperday', 6)
		self.intelligent_hours = bot.get('intelligentworkinghours', False)
		self.enable_instalike = bot.getboolean('instalike', True)
		self.enable_instafollow = bot.getboolean('instafollow', True)
		self.enable_instacomment = bot.getboolean('instacomment', False)
		self.enable_instamessage = bot.getboolean('instamessage', False)

		# INSTAGRAM SECTION
		self.instagram_username = instagram.get('username', None)
		self.instagram_password = instagram.get('password', None)

		