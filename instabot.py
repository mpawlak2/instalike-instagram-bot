import operation
import database
import period
import content
import instafollow
import instalike
import instaactivity
import configuration

import time

class InstaBot:
	def __init__(self, username, password):
		self.configuration = configuration.Configuration('default.cfg')
		
		self.username = self.configuration.instagram_username
		self.password = self.configuration.instagram_password

		self.operation = operation.Operations()
		self.data_source = database.DataSource(self.configuration.database_user, self.configuration.database_password, self.configuration.database_address, self.configuration.database_name)
		self.repository = database.Repository(self.data_source)
		self.content_manager = content.ContentManager(self.operation, self.repository, self.configuration)
		self.period_randomizer = period.PeriodRandomizer(self.configuration)

		# bots
		self.follow_bot = instafollow.InstaFollow(self.operation, self.repository, self.content_manager)
		self.like_bot = instalike.InstaLike(self.operation, self.repository, self.content_manager, self.configuration)
		self.activity_bot = instaactivity.InstaActivity(self.operation, self.repository, self.content_manager)

		# timing
		self.next_frame = 0
		self.start_time = time.time()
	
	def log_in(self):
		self.log('trying to log in ...')
		response = self.operation.log_in(self.username.lower(), self.password)

		if (response):
			self.log('logged in')
			return True
		else:
			self.log('oops! could not log in.')
		return False

	def log(self, text):
		print(text)

	def start(self):
		# we need valid configuration in order for bot to work properly
		if(not self.configuration.validate()):
			return False

		# generate 'random' periods of time
		self.period_randomizer.randomize()
		self.period_randomizer.info()

		while(not self.log_in()):
			print('failed to log in wait for 5min')
			time.sleep(5 * 60)

		while(True):
			if (self.period_randomizer.is_active()):
				if(self.configuration.enable_instalike):
						self.like_bot.act()

				if(self.configuration.enable_instafollow):
						self.follow_bot.act()
				self.activity_bot.act()
			time.sleep(1 / 60)

