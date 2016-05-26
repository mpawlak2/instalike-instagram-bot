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
		self.location = None
		self.owner = None

	def from_json(self, json_node):
		self.width = json_node['dimensions'].get('width', 0)
		self.height = json_node['dimensions'].get('height', 0)
		self.code = json_node['code']
		self.is_ad = json_node.get('is_ad', False)
		self.likes_count = json_node['likes']['count']
		self.viewer_has_liked = json_node['likes'].get('viewer_has_liked', False)
		self.is_video = json_node['is_video']
		self.id = json_node['id']
		self.display_src = json_node['display_src']
		self.location = json_node.get('location', 'null')
		self.caption = str(json_node['caption'])
		self.owner = User().from_json(json_node['owner'])
		return self

	def persist(self):
		pass


class User:
	def __init__(self):
		self.username = ''
		self.full_name = ''
		self.profile_pic_url = ''
		self.is_unpublished = False
		self.blocked_by_viewer = False
		self.id = 0
		self.is_private = False

	def from_json(self, json_node):
		self.username = json_node.get('username', 'null')
		self.full_name = json_node.get('full_name', 'null')
		self.profile_pic_url = json_node.get('profile_pic_url', 'null')
		self.is_unpublished = json_node.get('is_unpublished', 'null')
		self.blocked_by_viewer = json_node.get('blocked_by_viewer', 'null')
		self.id = json_node.get('id', 'null')
		self.is_private = json_node.get('is_private', 'null')
		return self

	def persist(self):
		pass
