import time
import random

import model

class InstaLike:

	def __init__(self, operation, repository, content_manager, configuration):
		self.operation = operation
		self.content_manager = content_manager
		self.repository = repository
		self.configuration = configuration

		self.max_likes_per_hour = self.configuration.instalike_max_likes_per_hour
		
		# Timing.
		self.next_like_time = 0
		self.like_time_delta = (60 * 60) // self.max_likes_per_hour

		# Instance stats.
		self.likes = 0
		self.failed_likes = 0
		self.hourly_likes = 0

		self.t0 = time.time()
		self.t1 = 0

	def like(self, media):
		response = self.operation.like(media.id)
		if(not response):
			return False

		if(response.status_code != 200):
			self.failed_to_like()
			return False

		self.repository.like(media, response.status_code)
		self.photo_liked()
		
		return True

	def act(self):
		if (not self.can_act()):
			return

		if (time.time() < self.next_like_time):
			return

		media = self.content_manager.get_next_media()
		self.like(media)

		self.like_timeout(self.like_time_delta - (self.like_time_delta // 2), self.like_time_delta + (self.like_time_delta // 2))

	def can_act(self):
		self.t1 = time.time()
		# hour elapsed
		if ((self.t1 - self.t0) >= 60 * 60):
			print('# of likes in last hour: {0}'.format(self.hourly_likes))
			self.t0 = time.time()
			self.hourly_likes = 0
			return True
		elif (self.hourly_likes > self.max_likes_per_hour):
			return False
		return True

	def like_timeout(self, mini, maxi):
		next_in = random.randint(mini, maxi)
		self.next_like_time = time.time() + next_in
		self.get_stats()

	def photo_liked(self):
		self.likes += 1
		self.hourly_likes += 1

	def failed_to_like(self):
		self.hourly_likes += 1
		self.failed_likes += 1

	def get_stats(self):
		self.t1 = time.time()
		per_hour = ((self.likes + self.failed_likes) * 60 * 60) // (1 if (self.t1 - self.t0) == 0 else self.t1 - self.t0)
		self.log('#######################################')
		self.log('----------------LIKES------------------')
		self.log('total time: {0:.0f}s'.format(self.t1 - self.t0))
		self.log('likes: {0}'.format(self.likes))
		self.log('failed likes: {0}'.format(self.failed_likes))
		self.log('estimated likes per hour: {0:.0f}'.format(per_hour))
		self.log('next like in: {0:.0f}s'.format(self.next_like_time - time.time()))
		self.log('photos to like: {0}'.format(self.content_manager.get_media_count()))

	def log(self, text):
		print(text)
