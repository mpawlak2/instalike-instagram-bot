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

	def store_user(self, user_model):
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
							id := {0},
							width := {1},
							height := {2},
							code := \'{3}\',
							is_ad := {4},
							likes_count := {5},
							viewer_has_liked := {6},
							is_video := {7},
							display_src := \'{8}\',
							location := {9})'''
		sql_query = sql_query.format(photo.id, photo.width, photo.height, photo.code, photo.is_ad, 
			photo.likes_count, photo.viewer_has_liked, photo.is_video, photo.display_src, photo.location)

		self.data_source.execute(sql_query)

		