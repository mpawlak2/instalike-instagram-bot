# bot that records follows & likes you receive.
class InstaActivity:
	def __init__(self, operation, repository, content_manager):
		self.operation = operation
		self.repository = repository
		self.content_manager = content_manager

		# instance stats
		self.follows = 0
		self.likes = 0
		
	def parse_activities(self):
		activities = self.content_manager.get_activity()
		