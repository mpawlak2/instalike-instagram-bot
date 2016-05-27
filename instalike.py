import time
import random

class InstaLike:

	def __init__(self, operation, repository, content_manager):
		self.operation = operation
		self.content_manager = content_manager
		self.repository = repository

		self.instagrams = []

		# CONFIGURATION BELOW
		self.max_likes_per_hour = 250
		
		# timing stuff
		self.next_like_time = 0

		# instance stats
		self.total_likes = 0
		self.hourly_likes = 0

	def like(self, photo):
		response = self.operation.like(photo['id'])
		# self.photo_repository.like(model.Photo().from_json(photo), response.status_code)

		if(response.status_code != 200):
			self.failed_to_like()
			return False
		self.photo_liked()
		return True

	def like_bot(self):
		if (len(self.instagrams) == 0):
			self.instagrams = random.sample(self.content_manager.get_photos(), 7)

		if (time.time() < self.next_like_time):
			return

		photo = self.instagrams.pop()
		if (self.like(photo)):
			self.log_event('liked photo!')

		self.update_like_timer(5, 15)


	def update_like_timer(self, mini, maxi):
		next_in = random.randint(mini, maxi)
		self.next_like_time = time.time() + next_in

	def photo_liked(self):
		self.total_likes += 1
		self.hourly_likes += 1

	def failed_to_like(self):
		self.hourly_likes += 1
		self.total_failed_likes += 1

	# def get_stats(self):
	# 	self.t1 = time.time()
	# 	per_hour = ((self.total_likes + self.total_failed_likes) * 60 * 60) // (1 if (self.t1 - self.t0) == 0 else self.t1 - self.t0)
	# 	self.log_event('==== stats ====')
	# 	self.log_event('total time [s]: {0}'.format(self.t1 - self.t0))
	# 	self.log_event('successful likes: {0}'.format(self.total_likes))
	# 	self.log_event('failed likes: {0}'.format(self.total_failed_likes))
	# 	self.log_event('estimated likes per hour: {0}'.format(per_hour))
	# 	if (per_hour > 350):
	# 		self.log_event('\tWARNING: liking more than 350 pics/h may result in blocked account.')
	# 	self.log_event('#######################################')

		

	# def log_event(self, text, nl = 1):
	# 	print(text)
		# sys.stdout.flush()
