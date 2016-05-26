import requests
import re
import json
import time
import sys
import random
import datetime
from operation import Operations
import spam
import model
import database

# ideas, obviously stolen :)
# progress
# like by tag (in progress)
# like by instagram account todo
# like by location todo
# like the newsfeed todo (like what people youre following post)
# like during specific times
# !! liking algorithm !! replicate human behavior likes at random
# follow back

# spam filter
# we want only real people to follow use
# deleting spam comments and follows


# new algorithm LIKE
# wait 45 - 90 mins before new operation
# like 1 - 5 posts / operation with delay 15-20s
# like max of 0 posts per day
# like between 12am - 12pm
# posted in last 90 days
# likes between 0 -500
# comments 0 - 500
# like in days of week

# like posts by keywords
# like posts of specific users
# like posts of followers
# has less tags than 4 i.e.
# like latest feed posts
# like by location

# new algorith COMMENT
# 90 and 180 min before operation
# 1-2 comments with delay 30-60s
# max per day
# times of day
# of week
# max comments per user

# repost tool
# scheulde posts for week

# get photos -> filter -> like -> wait -> get photos ?

# followed by profile that is not verified -> block user.
# get latest activity from feed.
# spam

# comment guard -> delete unwanted comments


class InstaLike:
	start_liking_at = 0 # 0 - 23 format
	stop_liking_at = 0 # 0 - 23 format

	tag_like = ['l4l']


	def __init__(self, login, password):
		self.login = login.lower()
		self.password = password

		# NOT CONFIGURATION BELOW
		self.operation = Operations()
		self.spam_validator = spam.SpamDetector(self.operation)
		self.loop_likes = 0
		self.loop_likes_fails = 0
		self.no_of_empty_tags = 0
		self.period_start = 0
		self.total_likes = 0
		self.current_likes = 0
		self.hourly_likes = 0
		self.period_time = 60 * 60
		self.instagrams = []
		# NOT CONFIGURATION ABOVE

		# DATABASE
		self.data_source = database.DataSource('postgres', 'postgres', 'localhost', 'instamanager')
		self.repository = database.Repository(self.data_source)

		# CONFIGURATION BELOW
		self.max_likes_per_hour = 245
		
		# timing stuff
		self.last_like_time = 0
		self.next_like_time = 0
		self.next_like_delta_time = 10 #
		
		self.last_response_fail_time = 0
		self.clear_fails_after_sec = 10 # after 10 seconds clear fail counter

		# loop stats
		self.t0 = 0
		self.t1 = 0

		# ban, access denied etc.
		self.ban400 = 0 # code: 400 responses
		self.response_fail = 0
		self.total_failed_likes = 0
		self.last_error_code = 200



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

	def get_photos(self):
		for tag in self.tag_like:
			self.log_event('getting posts from #{0} ...'.format(tag))
			self.instagrams.extend(self.operation.get_photos_by_tag(tag))

		if (self.instagrams):
			return True
		else:
			return False

	def filter_photos(self):
		# select randomly few photos
		how_many_to_like = random.randint(2,7)
		if (len(self.instagrams) < how_many_to_like):
			how_many_to_like = len(self.instagrams)

		if (how_many_to_like == 0):
			return

		self.instagrams = random.sample(self.instagrams, how_many_to_like)	

		self.log_event('trying to like {0} photos, selected randomly from a total of {1}'.format(how_many_to_like, len(self.instagrams)))

		self.instagrams = self.spam_validator.validate_photos(self.instagrams)

	# where photo is json parsed from instagram site.
	def like(self, photo):
		response = self.operation.like(photo['id'])
		
		if(response.status_code != 200):
			self.last_error_code = response.status_code
			if(response.status_code == 400):
				self.ban400 += 1
			self.failed_to_like()
			return False
		self.photo_liked()
		return True

	def like_bot(self):
		if (len(self.instagrams) == 0):
			self.log_event('operation completed')
			self.get_stats()
			self.get_photos()
			self.filter_photos()
			self.update_like_timer(10,30)

		if (time.time() < self.next_like_time):
			return # we have to wait more time

		photo = self.instagrams.pop()
		photo_model = model.Photo().from_json(photo)
		self.repository.merge_photo(photo_model)

		if (self.like(photo)):
			self.log_event('liked photo with id: {0}'.format(photo['id']))
		else:
			self.log_event('failed to like photo with id: {0}, status code: {1}'.format(photo['id'], self.last_error_code))
		self.update_like_timer(self.next_like_delta_time - 5, self.next_like_delta_time + 5)


	def update_like_timer(self, mini, maxi):
		next_in = random.randint(mini, maxi)
		self.log_event('next like attempt in {0} sec, {1} more photos to go.'.format(next_in, len(self.instagrams)))
		self.last_like_time = time.time()
		self.next_like_time = time.time() + next_in

	# like 2 - 7 random photos from collection
	# rest for 10 - 15s before every like
	def auto_liker(self):
		self.loop_likes = 0
		self.loop_likes_fails = 0

		how_many_to_like = random.randint(2,7)
		if (len(self.instagrams) < how_many_to_like):
			how_many_to_like = len(self.instagrams)

		if (how_many_to_like == 0):
			return

		self.log_event('trying to like {0} photos, selected randomly from a total of {1}'.format(how_many_to_like, len(self.instagrams)))


		photos = random.sample(self.instagrams, how_many_to_like)
		self.log_event('{0}/{1}\r'.format(0, how_many_to_like), 0)
		for photo in photos:
			if(self.like(photo)):
				self.loop_likes += 1
			else:
				self.loop_likes_fails += 1
			time.sleep(random.randint(8,15))
			self.log_event('{0}/{1}\r'.format(self.loop_likes + self.loop_likes_fails, how_many_to_like), 0)
		self.log_event('liked {0}/{1} instagrams, {2} fails'.format(self.loop_likes, how_many_to_like, self.loop_likes_fails))
		self.log_event('like operation complete; waiting for 15-30s')
		time.sleep(random.randint(15,30)) # so that rand select could mean something


	def wait_till_hour(self):
		if (self.start_liking_at > self.stop_liking_at or (self.start_liking_at == 0 and self.stop_liking_at == 0)):
			return

		now = datetime.datetime.now()
		if (now.hour > self.start_liking_at and now.hour < self.stop_liking_at):
			return

		# not in bounds -> wait
		sec_diff = 0

		if (now.hour < self.start_liking_at):
			self.log_event('too early - ', 0)
			wait_till = datetime.datetime(now.year, now.month, now.day, self.start_liking_at)
			sec_diff = (wait_till - now).seconds
		elif (now.hour > self.stop_liking_at):
			self.log_event('time to bed - ', 0)
			wait_till = datetime.datetime(now.year, now.month, now.day+1, self.start_liking_at)
			sec_diff = (wait_till - now).seconds

		if (sec_diff > 0):
			self.log_event('waiting for {0} min, till hour {1}'.format(sec_diff // 60, self.start_liking_at))
			time.sleep(sec_diff)

	def photo_liked(self):
		self.t1 = time.time()
		self.total_likes += 1
		self.hourly_likes += 1
		self.current_likes += 1

	def failed_to_like(self):
		self.hourly_likes += 1
		self.current_likes += 1
		self.response_fail += 1
		self.total_failed_likes += 1
		self.last_response_fail_time = time.time()

	def get_stats(self):
		self.t1 = time.time()
		per_hour = ((self.total_likes + self.total_failed_likes) * 60 * 60) // (1 if (self.t1 - self.t0) == 0 else self.t1 - self.t0)
		self.log_event('==== stats ====')
		self.log_event('total time [s]: {0}'.format(self.t1 - self.t0))
		self.log_event('successful likes: {0}'.format(self.total_likes))
		self.log_event('failed likes: {0}'.format(self.total_failed_likes))
		self.log_event('estimated likes per hour: {0}'.format(per_hour))
		if (per_hour > 350):
			self.log_event('\tWARNING: liking more than 350 pics/h may result in blocked account.')
		self.log_event('#######################################')

		


	def start(self):
		self.wait_till_hour()
		if(self.log_in() == False):
			self.log_event('Abort.')
			return False
		while(1==1):
			# self.wait_till_hour()
			self.like_bot()
			time.sleep(1 / 45) # 1s / 60 frames => 60fps

			# if(self.ban400 > 3):
			# 	self.log_event('You are banned?')
			# if(self.response_fail > 4):
			# 	self.log_event('Failed to like photo more than 4 times in short amount of time. Waiting for 10-15min.')
			# 	time.sleep(60*random.randint(10,15)) # 10 - 15 mins
			# 	self.response_fail = 0
			# 	self.log_in()
			# if (self.hourly_likes > self.max_likes_per_hour):
			# 	if (time.time() - self.period_start < self.period_time):
			# 		self.log_event('sleeping for {0} secs'.format(self.period_time - (time.time() - self.period_start)))
			# 		time.sleep(self.period_time - (time.time() - self.period_start))
			# 		self.period_start = time.time()
			# 		self.hourly_likes = 0
			# 	else:
			# 		# done under max in about hour
			# 		self.log_event('done under max in period')
			# 		self.hourly_likes = 0


	def log_event(self, text, nl = 1):
		print(text)
		# sys.stdout.flush()
