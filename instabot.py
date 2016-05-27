import operation
import database
import period
import content
import instafollow
import instalike

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

		self.next_frame = 0
	
	def log_in(self):
		response = self.operation.log_in(self.username.lower(), self.password)

		if (response):
			print('logged in')
			return True
		return False

	def start(self):
		self.period_randomizer.randomize()

		self.log_in()

		while(True):
			if (self.period_randomizer.is_active()):
				self.like_bot.act()
				self.follow_bot.act()
			time.sleep(1 / 60)

