import time
from random import randint

class InstaFollow:
	def __init__(self, operation, repository):
		self.operation = operation
		self.user_repository = repository

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

	def follow(self, user):
		response = self.operation.follow(user.id)

		if (response.status_code != 200):
			return False

		self.followed_successfully(user)
		return True

	def follow_bot(self):
		if (time.time() < self.next_follow_time):
			return

		user = self.users.pop()
		if (not self.follow(user))
			self.users.insert(0, user)

		self.update_timer()

	def update_timer(self):
		self.next_follow_time = time.time() + randint(self.min_wait_before_follow, self.max_wait_before_follow)


	def followed_successfully(self, user):
		self.user_repository.follow(self, user)
		self.total_follows += 1
		self.period_follows += 1
		