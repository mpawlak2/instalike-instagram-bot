import re

class SpamDetector:
	operation = object()
	photo_vaidator = object()

	# FOLLOWS

	# COMMENTS


	def __init__(self, op_object):
		self.operation = op_object
		self.photo_vaidator = PhotoValidator()

	def is_user_fake(self, user_id):
		pass

	def validate_photos(self, photos):
		filtered_photos = []

		for photo in photos:
			if (self.validate_photo(photo)):
				filtered_photos.append(photo)

		return filtered_photos

	# check if photo caption contains specified words
	def validate_photo(self, photo):
		if (self.photo_vaidator.illegal_photo_caption(photo))
			return False

		photo_details = self.operation.get_photo_details(photo['code'])
		if (photo_details):
			if (self.photo_vaidator.is_already_liked(photo_details)):
				return False
			if (self.photo_vaidator.illegal_owner_name(photo_details)):
				return False
			if (self.photo_vaidator.likes_limit(photo_details)):
				return False
		else:
			return False # could not load photo details
		return True



class PhotoValidator:
	# LIKES
	# ignore photos containing these tags, may regex here
	like_photo_caption_blacklist = ['#nude', '#fuck', '#ass', '#shit', '#.+?nude', '#.+?ass[\s#]', '#.+?fuck', '#followme', '#spam4spam', '#porn', '#tagsforlikes'] 

	# do not like photo if owner's username contains one of these words
	like_username_blacklist = ['porn', 'spam', 'nude', 'fuck']

	# do not like photo with more that this value likes, 0 - no limit
	like_max_likes = 24

	def is_already_liked(self, photo_details):
		return photo_details['likes'].get('viewer_has_liked', '?')

	def illegal_owner_name(self, photo_details):
		for bad_name in self.like_username_blacklist:
			match = re.search(bad_name, photo_details['owner']['username'])
			if (match):
				return True
		return False

	def illegal_photo_caption(self, photo):
		for bad_tag in self.like_photo_caption_blacklist:
			bad_words = re.search('#{0}'.format(bad_tag), photo.get('caption', ''))
			if (bad_words):
				return True
		return False

	def likes_limit(self, photo):
		return photo['likes']['count'] <= self.like_max_likes