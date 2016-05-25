import requests
import re
import json

class Operations:
	# url's
	base_url = 'https://www.instagram.com/'
	login_url = 'https://www.instagram.com/accounts/login/?force_classic_login&hl=pl'
	logout_url = 'https://www.instagram.com/accounts/logout/' # requires csrfmiddlewaretoken as payload
	like_url_tmpl = 'https://www.instagram.com/web/likes/{0}/like/'
	unlike_url_tmpl = 'https://www.instagram.com/web/likes/{0}/unlike/'
	follow_url_tmpl = 'https://www.instagram.com/web/friendships/{0}/follow/'
	unfollow_url_tmpl = 'https://www.instagram.com/web/friendships/{0}/unfollow/'
	comment_url_tmpl = 'https://www.instagram.com/web/comments/{0}/add/' # payload = { comment_text : 'wow'}
	tag_url = 'https://www.instagram.com/explore/tags/{0}/?__a=1'
	photo_details_url_tmpl = 'https://www.instagram.com/p/{0}/?__a=1' # in {0} goes the image code GET __a=1 - return only json

	# info
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
	accept_language = 'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4'
	content_type = 'application/x-www-form-urlencoded'


	session = requests.Session()

	headers = dict()
	ajx_headers = dict()
	cookies = dict()

	# this one has to be successful
	def log_in(self, user, password):
		payload = {
			'username' : user,
			'password' : password,
			'csrfmiddlewaretoken' : ''
		}

		# get unique csrftoken from server
		response = self.session.get(self.base_url)
		if (response.status_code != 200):
			print('error: {0}'.format(response.status_code))
			return None

		payload['csrfmiddlewaretoken'] = response.cookies['csrftoken']
		
		self.prepare_request(response)
		response = self.session.post(self.login_url, data = payload, headers = self.headers, allow_redirects = True)
		if (response.status_code != 200):
			print('could not log in. error: {0}'.format(response.status_code))
			return None
		return response

	def log_out(self):
		return self.session.post(self.logout_url, headers = self.headers, cookies = self.cookies)
		

	def is_logged_in(self):
		pass

	# dont use
	def prepare_ajax_request(self, request_response):
		self.ajx_headers = {
			'origin' : self.base_url,
			'referer' : request_response.url,
			'User-Agent' : self.user_agent,
			'content-type' : self.content_type,
			'accept-language' : self.accept_language,
			'accept-encoding' : 'gzip, deflate',
			'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'x-csrftoken' : request_response.cookies['csrftoken'],
			'x-instagram-ajax' : 1,
			'x-request-with' : 'XMLHttpRequest'
		}

	# dont use
	def prepare_request(self, request_response):
		self.headers = {
			'origin' : self.base_url,
			'referer' : request_response.url,
			'User-Agent' : self.user_agent,
			'content-type' : self.content_type,
			'accept-language' : self.accept_language,
			'accept-encoding' : 'gzip, deflate',
			'x-csrftoken' : request_response.cookies['csrftoken'],
			'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		}

		self.cookies = request_response.cookies
		self.prepare_ajax_request(request_response)

	def like(self, photo_id):
		return self.session.post(self.like_url_tmpl.format(photo_id), headers = self.ajx_headers, cookies = self.cookies)

	def unlike(self, photo_id):
		return self.session.post(self.unlike_url_tmpl.format(photo_id), headers = self.ajx_headers, cookies = self.cookies)

	def follow(self, user_id):
		return self.session.post(self.follow_url_tmpl.format(user_id), headers = self.ajx_headers, cookies = self.cookies)

	def unfollow(self, user_id):
		return self.session.post(self.unfollow_url_tmpl.format(user_id), headers = self.ajx_headers, cookies = self.cookies)

	def comment_photo(self, photo_id, comment):
		payload = {
			'comment_text' : comment
		}

		return self.session.post(self.comment_url_tmpl.format(photo_id), data = payload, headers = self.ajx_headers, cookies = self.cookies)

	
	def delete_my_comment(self, photo_id, comment_id):
		pass

	def delete_comment_uden_my_photo(self, photo_id, comment_id):
		pass

	def get_photos_by_tag(self, tag):
		response = self.session.get(self.tag_url.format(tag), headers = self.headers)
		if (response.status_code != 200):
			return None

		return json.loads(response.content.decode('utf-8'))['tag']['media']['nodes']

	def get_photo_details(self, photo_code):
		response = self.session.get(self.photo_details_url_tmpl.format(photo_code), headers = self.headers)

		if (response.status_code != 200):
			return None
		return json.loads(response.content.decode('utf-8'))['media']
		

	def get_my_followers(self):
		pass

	def get_my_following(self):
		pass

	def get_user_followers(self, user_id):
		pass

	def get_user_following(self, user_id):
		pass

	def get_user_info(self, user_id):
		pass

	def block_user(self, user_id):
		pass
		