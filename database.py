import postgresql
import log

class DataSource:
	def __init__(self, user, password, host, database_name):
		if (not self or not password or not host or not database_name):
			self.connection = None
		else:
			self.connection = postgresql.open('pq://{0}:{1}@{2}/{3}'.format(user, password, host, database_name))

	def execute(self, sql_query):
		self.connection.execute(sql_query)

	def prepare_procedure(self, procedure_signature):
		proc = self.connection.proc(procedure_signature)
		return proc



		
class Repository:
	def __init__(self, data_source):
		self.data_source = data_source
		self.logger = log.FileOutput('db_log.txt')

	def merge_user(self, user_model):
		sql_query = '''select merge_user(
						_id := {0},
						_username := {1},
						_has_blocked_viewer := {2},
						_follows_count := {3},
						_followed_by_count := {4},
						_external_url := {5},
						_follows_viewer := {6},
						_profile_pic_url := {7},
						_is_private := {8},
						_full_name := {9},
						_posts_count := {10},
						_blocked_by_viewer := {11},
						_followed_by_viewer := {12},
						_is_verified := {13}, 
						_biography := {14})'''
		sql_query = sql_query.format(
			user_model.id, 
			user_model.username, 
			user_model.has_blocked_viewer,
			user_model.follows_count,
			user_model.followed_by_count,
			user_model.external_url,
			user_model.follows_viewer,
			user_model.profile_pic_url,
			user_model.is_private,
			user_model.full_name,
			user_model.posts_count,
			user_model.blocked_by_viewer,
			user_model.followed_by_viewer,
			user_model.is_verified,
			user_model.biography)
		self.logger.log(sql_query.encode('utf-8'))
		self.data_source.execute(sql_query)

	def merge_photo(self, photo):
		sql_query = '''select merge_photo(
							_id := {0},
							_width := {1},
							_height := {2},
							_code := {3},
							_is_ad := {4},
							_likes_count := {5},
							_viewer_has_liked := {6},
							_is_video := {7},
							_display_src := {8},
							_location := {9})'''
		sql_query = sql_query.format(photo.id, photo.width, photo.height, photo.code, photo.is_ad, 
			photo.likes_count, photo.viewer_has_liked, photo.is_video, photo.display_src, photo.location)
		self.logger.log(sql_query.encode('utf-8'))
		self.data_source.execute(sql_query)

	def like(self, photo_model, status_code):
		sql_query = 'select like_photo(_photo_id := {0}, _status_code := {1})'
		sql_query = sql_query.format(photo_model.id, status_code)
		self.logger.log(sql_query.encode('utf-8'))
		self.data_source.execute(sql_query)

	def follow(self, user, status_code):
		sql_query = 'select follow_user(_user_id := {0}, _status_code := {1})'
		sql_query = sql_query.format(user.id, status_code)
		self.logger.log(sql_query.encode('utf-8'))
		self.data_source.execute(sql_query)

	def register_activity(self, activity):
		sql_query = 'select register_activity(_type := {0}, _user_id := {1}, _activity_time := {2})'
		sql_query = sql_query.format(activity.type, activity.user_id, activity.timestamp)
		self.logger.log(sql_query.encode('utf-8'))
		self.data_source.execute(sql_query)

	def get_users_to_unfollow(self):
		proc = self.data_source.prepare_procedure('get_users_to_unfollow()')
		return proc()

		