import requests
import re
import json
import time
import sys
from random import randint

class InstaLike:
	login_url = 'https://www.instagram.com/accounts/login/?force_classic_login&hl=pl'
	tag_url = 'https://www.instagram.com/explore/tags/{0}/'
	like_url = 'https://www.instagram.com/web/likes/{0}/like/'
	base_url = 'https://www.instagram.com/'

	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
	accept_language = 'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4'
	content_type = 'application/x-www-form-urlencoded'

	instagrams = ''
	headers = ''
	cookies = ''

	response_fail = 0
	total_failed_likes = 0
	ban400 = 0

	# instance stats
	t0 = 0
	t1 = 0
	total_likes = 0
	# after # of likes rest for 5h or whatever
	current_likes = 0

	def __init__(self, login, password):
		self.session = requests.Session()
		self.login = login.lower()
		self.password = password

	def log_in(self):
		self.payload = {
			'username' : self.login,
			'password' : self.password,
			'csrfmiddlewaretoken' : ''
		}

		# get csrftoken
		response = self.session.get(self.base_url)
		self.csrftoken = response.cookies['csrftoken']
		self.payload['csrfmiddlewaretoken'] = self.csrftoken

		# setup headers
		self.headers = {
			'origin' : self.base_url,
			'referer' : self.login_url,
			'User-Agent' : self.user_agent,
			'upgrade-insecure-requests' : 1,
			'content-length' : 97,
			'content-type' : self.content_type,
			'cache-control' : 'max-age=0',
			'accept-language' : self.accept_language,
			'accept-encoding' : 'gzip, deflate',
			'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		}

		self.log_event('Trying to log in with credentials: username = "{0}" and password = "{1}"'.format(self.payload['username'], self.payload['password']))

		# try to log in
		response = self.session.post(self.login_url, data = self.payload, headers = self.headers, allow_redirects = True)
		if (response.status_code != 200):
			self.log_event('Could not log in, status code: {0}'.format(response.status_code))
			return False
		else:
			self.headers['referer'] = response.url
			self.t0 = time.time()
			self.log_event('Logged in successfully.')
			# was redirected
			if (len(response.history) > 0):
				self.log_event('\tHistory: {0}'.format(response.history))
			return True

	def get_instagrams(self):
		self.log_event('getting posts...')
		response = self.session.get(self.tag_url.format('l4l'), headers = self.headers)
		if (response.status_code != 200):
			self.log_event('Could not get instagrams. Status code: {0}'.format(response.status_code))
			return False

		self.headers = {
			'accept' : '*/*',
			'accept-encoding' : 'gzip, deflate',
			'accept-language' : self.accept_language,
			'content-length' : 0,
			'origin' : self.base_url,
			'referer' : response.url,
			'user-agent' : self.user_agent,
			'x-csrftoken' : response.cookies['csrftoken'],
			'x-instagram-ajax' : 1,
			'x-request-with' : 'XMLHttpRequest'
		}

		self.cookies = response.cookies

		posts = re.search(b'_sharedData = ({.+?});</script>', response.content)
		if(posts):
			self.instagrams = json.loads(posts.group(1).decode('utf-8'))['entry_data']['TagPage'][0]['tag']['media']['nodes']
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
		last_error = 'none'
		for instagram in self.instagrams:
			if(instagram['likes']['count'] < 10):
				response = self.session.post(self.like_url.format(instagram['id']), headers = self.headers, cookies = self.cookies, allow_redirects = True)
				# status code == 400 -> youre fucked! BAN.
				if(response.status_code != 200):
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
				self.log_event('Failed to like photo more than 4 times. Waiting for some time.')
				time.sleep(10*randint(6,9))
				self.response_fail = 0
				self.log_in()
			if(self.get_instagrams()):
				self.like()
				self.get_stats()


	def log_event(self, text, nl = 1):
		sys.stdout.write(text + ('\n' if nl == 1 else ''))
		sys.stdout.flush()
