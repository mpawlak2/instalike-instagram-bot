import time
from random import randint

class InstaFollow:
	def __init__(self, operation, repository, content_manager):
		self.operation = operation
		self.user_repository = repository
		self.content_manager = content_manager

		# configuration
		self.max_daily_follows = 200
		self.max_daily_unfollows = 300

		# users
		self.users = []

		# instance stats
		self.total_follows = 0
		self.period_follows = 0

		# timing
		self.next_follow_time = 0
		self.min_wait_before_follow = 10
		self.max_wait_before_follow = 300

	def follow(self, user_id):
		response = self.operation.follow(user_id)

		if (response.status_code != 200):
			return False

		self.followed_successfully(user_id)
		return True

	def act(self):
		if (len(self.users) == 0):
			self.users = self.content_manager.get_users()
		if (time.time() < self.next_follow_time):
			return

		user = self.users.pop()
		if (not self.follow(user)):
			self.users.insert(0, user)
		else:
			print('user followed')

		self.update_timer()

	def update_timer(self):
		self.next_follow_time = time.time() + randint(self.min_wait_before_follow, self.max_wait_before_follow)


	def followed_successfully(self, user_id):
		# self.user_repository.follow(self, user_id)
		self.total_follows += 1
		self.period_follows += 1
		