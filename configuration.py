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
		notification = self.config['NOTIFICATIONS']
		ban = self.config['BAN']
		database = self.config['DATABASE']
		instalike = self.config['INSTALIKE']
		instafollow = self.config['INSTAFOLLOW']

		# BOT SECTION
		self.bot_work_hours = bot.get('workhoursperday', 6)
		self.intelligent_hours = bot.get('intelligentworkinghours', False)
		self.enable_instalike = bot.getboolean('instalike', True)
		self.enable_instafollow = bot.getboolean('instafollow', True)
		self.enable_instacomment = bot.getboolean('instacomment', False)
		self.enable_instamessage = bot.getboolean('instamessage', False)

		# NOTIFICATIONS SECTION
		self.notification_enable_email = notification.getboolean('enableemailsummarynotifications', False)
		self.notification_send_attachment = notification.getboolean('sendattachment', False)
		self.notification_email_address = notification.get('emailadress', None)

		# BAN SECTION
		self.avoid_bans = ban.getboolean('donotgetbanned', False)

		# INSTAGRAM SECTION
		self.instagram_username = instagram.get('username', None)
		self.instagram_password = instagram.get('password', None)

		# DATABASE
		self.enable_database = database.getboolean('usedatabase', True)
		self.database_name = database.get('databasename', 'instamanager')
		self.database_user = database.get('username', None)
		self.database_password = database.get('password', None)

		# INSTALIKE
		self.instalike_max_likes_per_hour = int(instalike.get('maxlikesperhour', 160))
		self.instalike_tags = instalike.get('tags', None)

		# INSTAFOLLOW
		self.instafollow_max_follows_per_hour = int(instafollow.get('maxfollowsperhour', 8))
		self.instafollow_max_unfollows_per_hour = int(instafollow.get('maxunfollowsperhour', 2))
		self.instafollow_unfollow_who_does_not_follow_back = instafollow.getboolean('unfollowwhennotfollowingback', True)

	def validate(self):
		if(not self.instagram_username or not self.instagram_password):
			print('You have to provide instagram username and password under INSTAGRAM section in default.cfg file.')
			return False

		if(self.enable_database):
			if(not self.database_user or not self.database_password):
				print('You have to provide database username and password or disable database use under DATABASE section in default.cfg file.')
				return False

		# validate instalike configuration
		if(self.enable_instalike):
			if(not self.instalike_tags):
				print('You have to provide tags under INSTALIKE section in default.cfg file.')
				return False
		
		# all fine
		return True
