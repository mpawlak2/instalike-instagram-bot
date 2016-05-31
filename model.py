class Photo:
	def __init__(self):
		self.width = 0
		self.height = 0
		self.code = ''
		self.is_ad = False
		self.likes_count = 0
		self.viewer_has_liked = False
		self.is_video = False
		self.id = 0
		self.display_src = ''
		self.location = 'null'
		self.owner_id = 'null'
		self.caption = 'null'
		self.owner_username = 'null'

	def from_json(self, json_node):
		self.width = json_node['dimensions'].get('width', 0)
		self.height = json_node['dimensions'].get('height', 0)
		self.code = self.mark_as_text(json_node['code'])
		self.is_ad = json_node.get('is_ad', False)
		self.likes_count = json_node['likes']['count']
		self.viewer_has_liked = json_node['likes'].get('viewer_has_liked', False)
		self.is_video = json_node['is_video']
		self.id = json_node['id']
		self.display_src = self.mark_as_text(json_node['display_src'])
		self.location = self.mark_as_text(self.try_get_location(json_node))
		self.caption = self.mark_as_text(json_node.get('caption', 'null'))
		self.owner_id = json_node['owner'].get('id', 'null')
		self.owner_username = self.mark_as_text(json_node['owner'].get('username', 'null')) # nie mozna wyszukac uzytownika po 'username' powinno byc tylko username
		return self

	def try_get_location(self, json_node):
		loc = json_node.get('location', 'null')
		if (loc == 'null' or loc == None):
			return 'null'
		loc = loc.get('name', 'null')
		if (loc == 'null'):
			return 'null'
		return loc

	def mark_as_text(self, text):
		if (text == None or text == 'null'):
			return 'null'
		else:
			text = text.replace('\'','')
		return '\'' + text + '\''

class User:
	def __init__(self):
		self.id = 0
		self.username = 'null'
		self.has_blocked_viewer = False
		self.follows_count = 0
		self.followed_by_count = 0
		self.external_url = 'null'
		self.follows_viewer = False
		self.profile_pic_url = 'null'
		self.is_private = False
		self.full_name = 'null'
		self.posts_count = 0
		self.blocked_by_viewer = False
		self.followed_by_viewer = False
		self.is_verified = False
		self.biography = 'null'

	def from_json(self, json_node):
		self.username = self.mark_as_text(json_node.get('username', 'null'))
		self.has_blocked_viewer = json_node.get('has_blocked_viewer', False)
		self.follows_count = json_node['follows'].get('count', 0)
		self.followed_by_count = json_node['followed_by'].get('count', 0)
		self.external_url = self.mark_as_text(json_node.get('external_url', 'null'))
		self.follows_viewer = json_node.get('follows_viewer', False)
		self.profile_pic_url = self.mark_as_text(json_node.get('profile_pic_url', 'null'))
		self.is_private = json_node.get('is_private', False)
		self.full_name = self.mark_as_text(json_node.get('full_name', 'null'))
		self.posts_count = json_node['media'].get('count', 0)
		self.blocked_by_viewer = json_node.get('blocked_by_viewer', False)
		self.followed_by_viewer = json_node.get('follows_viewer', False)
		self.is_verified = json_node.get('is_verified', False)
		self.id = json_node.get('id', 'null')
		bio = json_node.get('biography', 'null')
		self.biography = self.mark_as_text('null' if bio == None else bio.replace('\'',''))

		return self

	def mark_as_text(self, text):
		if (text == None or text == 'null'):
			return 'null'
		else:
			text = text.replace('\'','')
		return '\'' + text + '\''

class Activity:
	def __init__(self):
		self.timestamp = 'null'
		self.user_id = 0
		self.type = 0

	def from_json(self, json_node):
		self.timestamp = self.mark_as_text(json_node.get('timestamp', 'null'))
		self.type = json_node.get('type', 0)
		self.user_id = json_node['user'].get('pk', 0)
		return self

	def mark_as_text(self, text):
		if (text == None or text == 'null'):
			return 'null'
		else:
			text = text.replace('\'','')
		return '\'' + text + '\''