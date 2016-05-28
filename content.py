import spam

class ContentManager:
	def __init__(self, operation, repository):
		self.operation = operation
		self.repository = repository
		self.spam_validator = spam.SpamDetector(self.operation, self.repository)

		self.tags = ['l4l', 'f4f']

		self.photos = []
		self.user_ids = []

	def get_photos(self):
		# get by tags
		for tag in self.tags:
			try:
				print('getting photos from tag {0}...'.format(tag))
				self.photos = self.operation.get_photos_by_tag(tag)
			except TypeError:
				print('oops! someting went wrong while fetching photos')

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
		self.photos = self.spam_validator.validate_photos(self.photos)
		print('downloaded {0} valid photos'.format(len(self.photos)))
		