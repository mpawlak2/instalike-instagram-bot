import configparser

import sys
import getopt

class Configuration:
	def __init__(self, filename):
		self.validated = True
		self.config = configparser.ConfigParser()
		self.config.read(filename)

		self.args = sys.argv[1:]

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
		blacklist = self.config['BLACKLIST']
		likefilter = self.config['LIKEFILTER']

		# BOT SECTION
		self.bot_work_whole_time = bot.getboolean('workwholetime', False)
		self.bot_stop_after_minutes = bot.get('stopafternumerOfminutes', 0)
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
		self.database_address = database.get('address', 'localhost')

		# INSTALIKE
		self.instalike_max_likes_per_hour = int(instalike.get('maxlikesperhour', 160))
		self.instalike_tags = instalike.get('tags', None)

		# INSTAFOLLOW
		self.instafollow_max_follows_per_hour = int(instafollow.get('maxfollowsperhour', 8))
		self.instafollow_max_unfollows_per_hour = int(instafollow.get('maxunfollowsperhour', 2))
		self.instafollow_unfollow_users = instafollow.getboolean('UnfollowUsers', False)
		self.instafollow_unfollow_after_days = int(instafollow.get('UnfollowAfterNoOfDays', 6))

		# BLACKLIST
		self.banned_tags = blacklist.get('PhotoTagsList', None)
		self.banned_words_in_user_desc = blacklist.get('UserDescription', None)

		# LIKEFILTER
		self.like_min_likes_on_photo = int(likefilter.get('MinLikesOnPhoto', 0))
		self.like_max_likes_on_photo = int(likefilter.get('MaxLikesOnPhoto', 0))

		if (not self.banned_tags):
			self.banned_tags = []
		else:
			self.banned_tags = list(map(lambda tag: '#' + tag.strip(), self.banned_tags.split(',')))

		if (not self.banned_words_in_user_desc):
			self.banned_words_in_user_desc = []
		else:
			self.banned_words_in_user_desc = list(map(lambda tag: tag.strip(), self.banned_words_in_user_desc.split(',')))

	def validate(self):
		# override default.cfg username and password settings if provided via command line
		if(len(self.args) > 0):
			try:
				opts, args = getopt.getopt(self.args, 'u:p:')
			except getopt.GetoptError:
				print('Usage: main.py -u username -p password')
				return False
			if(len(opts) != 2):
				print('Usage: main.py -u username -p password')
				return False
			for opt, arg in opts:
				if(opt == '-u'):
					self.instagram_username = arg
				if(opt == '-p'):
					self.instagram_password = arg
		
		self.check_Constraint(self.instafollow_unfollow_users and not self.enable_database, 'Unfollowing users wont work without database.', 1)
		self.check_Constraint(self.instalike_max_likes_per_hour > 200, 'High likes per hour may result in blocked account.', 1)
		self.check_Constraint(self.instafollow_max_follows_per_hour > 10, 'High follows per hour may result in blocked account.', 1)
		self.check_Constraint(self.instafollow_max_unfollows_per_hour > 10, 'High unfollows per hour may result in blocked account.', 1)
		self.check_Constraint(not self.instagram_username or not self.instagram_password, 'You have to provide instagram username and password under INSTAGRAM section in default.cfg file.', 2)
		self.check_Constraint(self.enable_database and (not self.database_user or not self.database_password), 'You have to provide database username and password or disable database use under DATABASE section in default.cfg file.', 2)
		self.check_Constraint(self.enable_instalike and not self.instalike_tags, 'default.cfg, section: INSTALIKE, option: tags - you have to provide tags that bot can use to download media', 2)
		self.check_Constraint(self.like_min_likes_on_photo > self.like_max_likes_on_photo, 'default.cfg, section: LIKEFILTER, option: MinLikesOnPhoto & MaxLikesOnPhoto - max likes should be greater than min likes.', 2)
		self.check_Constraint(self.bot_work_whole_time, 'bot is working whole time, be careful because leaving it running for too long time may result in blocked account.', 1)

		return self.validated

	# condition - when true displays message
	# message - message to display
	# error_type - 1 - WARNING, 2 - ERROR
	def check_Constraint(self, condition, message, error_type):
		if(condition):
			print(('WARNING! ' if error_type == 1 else 'ERROR! ') + message)
			if(error_type == 2):
				self.validated = False
				print('Correct errors and start bot again.')

