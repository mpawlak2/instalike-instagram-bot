import random

import spam
import model

class ContentManager:
	def __init__(self, operation, repository):
		self.operation = operation
		self.repository = repository
		self.spam_validator = spam.SpamDetector(self.operation, self.repository)

		self.tags = ['l4l', 'f4f']

		self.photos = []
		self.photos_from_model = []
		self.users_from_model = []
		self.user_ids = []
		self.data_from_tags = []

	def get_photos(self):
		self.photos_from_model = []
		self.users_from_model = []

		no_of_photos = random.randint(2,10)

		for tag in self.tags:
			try:
				print('getting photos from tag {0}...'.format(tag))
				self.photos = self.operation.get_photos_by_tag(tag)
			except TypeError:
				print('oops! someting went wrong while fetching photos')

		# get details for each photo
		for photo in self.photos:
			photo_details = self.operation.get_photo_details(photo['code'])
			if (photo_details):
				photo_instance = model.Photo().from_json(photo_details)
				self.repository.merge_photo(photo_instance)
				self.photos_from_model.append(photo_instance)

			user_details = self.operation.get_user_details(photo_instance.owner_username.replace('\'',''))
			if (user_details):
				user_instance = model.User().from_json(user_details)
				self.repository.merge_user(user_instance)
				self.users_from_model.append(user_instance)

		self.filter_photos()

		return self.photos_from_model

	def get_users(self):
		return self.users_from_model

	def filter_photos(self):
		self.photos_from_model = self.spam_validator.validate_photos(self.photos_from_model)
		print('downloaded {0} valid photos'.format(len(self.photos)))
		