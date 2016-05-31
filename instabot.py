import operation
import database
import period
import content
import instafollow
import instalike
import instaactivity

import time

class InstaBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password

		self.operation = operation.Operations()
		self.data_source = database.DataSource('postgres', 'postgres', 'localhost', 'instamanager')
		self.repository = database.Repository(self.data_source)
		self.content_manager = content.ContentManager(self.operation, self.repository)
		self.period_randomizer = period.PeriodRandomizer()

		# bots
		self.follow_bot = instafollow.InstaFollow(self.operation, self.repository, self.content_manager)
		self.like_bot = instalike.InstaLike(self.operation, self.repository, self.content_manager)
		self.activity_bot = instaactivity.InstaActivity(self.operation, self.repository, self.content_manager)

		self.next_frame = 0
	
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
		self.period_randomizer.randomize()
		self.period_randomizer.info();

		while(not self.log_in()):
			print('failed to log in wait for 5min')
			time.sleep(5 * 60)

		while(True):
			if (self.period_randomizer.is_active()):
				self.like_bot.act()
				self.follow_bot.act()
				self.activity_bot.act()
			time.sleep(1 / 60)

