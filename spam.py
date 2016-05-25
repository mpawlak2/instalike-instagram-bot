class SpamDetector:
	operation = object()

	def __init__(self, op_object):
		self.operation = op_object
		
	def is_user_fake(self, user_id):
		user = self.operation.get_user_info(user_id)

		if (self.user_is_not_verified(user) or self.user_has_followers_but_did_not_post_anything(user))
			self.operation.block_user(user_id)

	def user_is_not_verified(self, user):
		return user['verified'] == 'false'

	def user_has_followers_but_did_not_post_anything(self, user):
		return user['likes'] > 1000 and user['posts']['count'] == 0

	def users_followers_are_at_least_two_times_following(self, user):
		return user['followers']['count'] > 2 * user['following']['count']