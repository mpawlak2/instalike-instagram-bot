import requests
import re
import json
import time
import sys
from random import randint
from operation import Operations

class InstaLike:
	operation = Operations()

	instagrams = ''

	response_fail = 0
	total_failed_likes = 0
	ban400 = 0

	# instance stats
	t0 = 0
	t1 = 0

	period_start = 0
	period_time = 60 * 60

	total_likes = 0
	current_likes = 0
	max_likes_per_hour = 245
	hourly_likes = 0

	def __init__(self, login, password):
		self.session = requests.Session()
		self.login = login.lower()
		self.password = password

	def log_in(self):
		self.log_event('trying to log in')

		response = self.operation.log_in(self.login, self.password)

		if (not response):
			self.log_event('Could not log in, status code: {0}'.format(response.status_code))
			return False
		else:
			self.t0 = time.time()
			self.period_start = time.time()
			self.log_event('Logged in successfully.')
			return True

	def get_instagrams(self):
		self.log_event('getting posts...')
		self.instagrams = self.operation.get_photos_by_tag('l4l')

		if (self.instagrams):
			self.log_event('found {0} posts matching criteria out of {1}'.format(len(list(filter(lambda x : x['likes']['count'] < 10, self.instagrams))), len(self.instagrams)))
			time.sleep(randint(5,7))
			return True
		else:
			self.log_event('Could not find any posts.')
			return False

	def like(self):
		to_like = len(list(filter(lambda x : x['likes']['count'] < 10, self.instagrams)))
		liked = 0
		self.current_likes = 0
		self.response_fail = 0 # count fails that happen to occur in short amount of time
		last_error = 'none'
		for instagram in self.instagrams:
			if(instagram['likes']['count'] < 100):
				# todo
				# self.log_event(instagram['likes'].get('viewer_has_liked', 'false'))
				response = self.operation.like(instagram['id'])
				# status code == 400 -> youre fucked! BAN.
				if(response.status_code != 200):
					self.hourly_likes += 1
					self.current_likes += 1
					last_error = response.status_code
					if(response.status_code == 400):
						self.ban400 += 1
					self.response_fail += 1
					self.total_failed_likes += 1
					continue

				# update stats
				self.t1 = time.time()
				liked += 1
				self.total_likes += 1
				self.hourly_likes += 1
				self.current_likes += 1
				self.log_event('{0}/{1}\r'.format(self.current_likes, to_like), 0)
				time.sleep(randint(1,3))
		self.log_event('liked {0}/{1} instagrams, {2} fails, last error code: {3}'.format(liked, to_like, to_like - liked, last_error))

	def get_stats(self):
		per_hour = ((self.total_likes + self.total_failed_likes) * 60 * 60) // (self.t1 - self.t0)
		self.log_event('total time [s]: {0}'.format(self.t1 - self.t0))
		self.log_event('total likes: {0}'.format(self.total_likes))
		self.log_event('estimated likes per hour: {0}'.format(per_hour))
		if (per_hour > 350):
			self.log_event('\tWARNING: liking more than 350 pics/h may result in blocked account.')
		self.log_event('total failed likes: {0}'.format(self.total_failed_likes))
		self.log_event('#######################################')

		


	def start(self):
		if(self.log_in() == False):
			self.log_event('Abort.')
			return False
		while(1==1):
			if(self.ban400 > 3):
				self.log_event('You are banned?')
			if(self.response_fail > 4):
				self.log_event('Failed to like photo more than 4 times in short amount of time. Waiting for some time.')
				time.sleep(10*randint(6,9))
				self.response_fail = 0
				self.log_in()
			if(self.get_instagrams()):
				self.like()
				self.get_stats()
			if (self.hourly_likes > self.max_likes_per_hour):
				if (time.time() - self.period_start < self.period_time):
					self.log_event('sleeping for {0} secs'.format(self.period_time - (time.time() - self.period_start)))
					time.sleep(self.period_time - (time.time() - self.period_start))
					self.period_start = time.time()
					self.hourly_likes = 0
				else:
					# done under max in about hour
					self.log_event('done under max in period')
					self.hourly_likes = 0


	def log_event(self, text, nl = 1):
		sys.stdout.write(text + ('\n' if nl == 1 else ''))
		sys.stdout.flush()
