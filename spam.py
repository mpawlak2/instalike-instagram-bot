import re

##
import model

class SpamDetector:
	def __init__(self, op_object, repository, configuration):
		self.operation = op_object
		self.repository = repository
		self.photo_vaidator = PhotoValidator(configuration.banned_tags, configuration.banned_words_in_user_desc, configuration.like_min_likes_on_photo, configuration.like_max_likes_on_photo)
		self.user_validator = UserValidator(configuration.banned_words_in_user_desc)

	def is_user_fake(self, user_id):
		pass

	def validate_users(self, users):
		valid_users = []
		for user in users:
			if(self.user_validator.is_valid(user)):
				valid_users.append(user)
		return valid_users

	def validate_photos(self, photos):
		filtered_photos = []
		self.log('validating {0} photos'.format(len(photos)))
		for photo in photos:
			if (self.validate_photo(photo)):
				filtered_photos.append(photo)

		self.log('filtered {0} valid photos out of {1}'.format(len(filtered_photos), len(photos)))
		return filtered_photos

	# check if photo caption contains specified words
	def validate_photo(self, photo):
		if (not photo):
			return False

		if (self.photo_vaidator.illegal_photo_caption(photo)):
			self.log('photo removed - illegal tags')
			return False

		if (self.photo_vaidator.is_already_liked(photo)):
			self.log('photo removed - already liked')
			return False

		if (self.photo_vaidator.illegal_owner_name(photo)):
			self.log('photo removed - illegal owners name')
			return False

		if (self.photo_vaidator.like_limit_exceeded(photo)):
			self.log('photo removed - like limit exceeded')
			return False
		
		# persist photos that you actually may like
		self.repository.merge_photo(photo)

		return True

	def log(self, message):
		print(message)


class UserValidator:
	def __init__(self, banned_description):
		self.username_blacklist = ['nude']
		self.description_blacklist = banned_description

		self.min_followers = 50
		self.min_following = 50

	def is_valid(self, user):
		return self.is_in_follow_bounds(user) and self.is_not_already_followed(user) and not self.illegal_username(user) and not self.illegal_user_bio(user)

	def is_in_follow_bounds(self, user):
		if (user.follows_count > self.min_following and user.followed_by_count > self.min_followers):
			return True
		return False

	def is_not_already_followed(self, user):
		return not user.followed_by_viewer

	def illegal_username(self, user):
		for bad_word in self.username_blacklist:
			match = re.search(bad_word, user.username)
			if (match):
				return True

		return False

	def illegal_user_bio(self, user):
		for bad_word in self.description_blacklist:
			match = re.search(bad_word, user.biography)
			if (match):
				return True

		return False

		


class PhotoValidator:
	def __init__(self, banned_tags, banned_description, min_likes, max_likes):
		# LIKES
		# ignore photos containing these tags, may regex here
		self.like_photo_caption_blacklist = banned_tags

		# do not like photo if owner's username contains one of these words
		self.like_username_blacklist = banned_description

		# do not like photo with more that this value likes, 0 - no limit
		self.like_max_likes = max_likes
		self.like_min_likes = min_likes

	def is_already_liked(self, photo):
		return photo.viewer_has_liked

	def illegal_owner_name(self, photo):
		for bad_name in self.like_username_blacklist:
			match = re.search(bad_name, photo.owner_username)
			if (match):
				return True
		return False

	def illegal_photo_caption(self, photo):
		for bad_tag in self.like_photo_caption_blacklist:
			bad_words = re.search('{0}'.format(bad_tag), photo.caption)
			if (bad_words):
				return True
		return False

	def like_limit_exceeded(self, photo):
		return (photo.likes_count > self.like_max_likes and self.like_max_likes != 0) or (photo.likes_count < self.like_min_likes and self.like_min_likes != 0)