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

		for tag in self.tags:
			try:
				print('getting photos from tag {0}...'.format(tag))
				self.photos = self.operation.get_photos_by_tag(tag)
			except TypeError:
				print('oops! someting went wrong while fetching photos')

		# get details for each photo
		for photo in self.photos:
			photo_details = self.operation.get_photo_details(photo['code'])
			photo_instance = model.Photo().from_json(photo_details)
			self.repository.merge_photo(photo_instance)

			user_details = self.operation.get_user_details(photo_instance.owner_username)
			user_instance = model.User().from_json(user_details)
			self.users_from_model.append(user_instance)
			self.repository.merge_user(user_instance)

			self.photos_from_model.append(photo_instance)
			print(user_instance.follows_count)

		self.filter_photos()

		return self.photos

	def get_users(self):
		if (len(self.photos) > 0):
			self.user_ids = list(map(lambda x : x['owner']['id'], self.photos))
			return self.user_ids
		self.get_photos()
		self.user_ids = list(map(lambda x : x['owner']['id'], self.photos))
		return self.user_ids

	def filter_photos(self):
		self.photos_from_model = self.spam_validator.validate_photos(self.photos_from_model)
		print('downloaded {0} valid photos'.format(len(self.photos)))
		