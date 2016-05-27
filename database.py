import postgresql

class DataSource:
	def __init__(self, user, password, host, database_name):
		if (not self or not password or not host or not database_name):
			self.connection = None
		else:
			self.connection = postgresql.open('pq://{0}:{1}@{2}/{3}'.format(user, password, host, database_name))

	def execute(self, sql_query):
		self.connection.execute(sql_query)

		
class Repository:
	def __init__(self, data_source):
		self.data_source = data_source

	def merge_user(self, user_model):
		sql_query = '''select merge_user(
							id := {0}, 
							username := {1}, 
							full_name := {2}, 
							profile_pic_url := {3}, 
							is_unpublished := {4}, 
							blocked_by_viewer := {5}, 
							is_private := {6}'''
		sql_query = sql_query.format(user_model.id, user_model.username, user_model.full_name, user_model.profile_pic_url, user_model.is_unpublished, user_model.blocked_by_viewer, user_model.is_private)
		self.data_source.execute(sql_query)

	def merge_photo(self, photo):
		sql_query = '''select merge_photo(
							_id := {0},
							_width := {1},
							_height := {2},
							_code := \'{3}\',
							_is_ad := {4},
							_likes_count := {5},
							_viewer_has_liked := {6},
							_is_video := {7},
							_display_src := \'{8}\',
							_location := {9})'''
		sql_query = sql_query.format(photo.id, photo.width, photo.height, photo.code, photo.is_ad, 
			photo.likes_count, photo.viewer_has_liked, photo.is_video, photo.display_src, photo.location)
		self.data_source.execute(sql_query)


class PhotoRepository:
	def __init__(self, data_source):
		self.data_source = data_source

	def like(self, photo_model, status_code):
		sql_query = 'select like_photo(_photo_id := {0}, _status_code := \'{1}\')'
		sql_query = sql_query.format(photo_model.id, status_code)
		self.data_source.execute(sql_query)
		

		