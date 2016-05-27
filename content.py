
class ContentManager:
	def __init__(self, operation):
		self.operation = operation

		self.tags = ['l4l', 'f4f']

		self.photos = []
		self.user_ids = []

	def get_photos(self):
		if (len(self.photos) > 0):
			return self.photos

		# get by tags
		for tag in self.tags:
			try:
				self.photos.extend(self.operation.get_photos_by_tag(tag))
			except TypeError:
				self.log_event('oops! someting went wrong while fetching photos')

		return self.photos

	def get_users(self):
		if (len(self.photos) > 0):
			self.user_ids = map(lambda x : x['owner']['id'], self.photos)
			return self.user_ids
		self.get_photos()
		self.user_ids = map(lambda x : x['owner']['id'], self.photos)
		return self.user_ids



		