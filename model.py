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
		self.is_ad = json_node['is_ad']
		self.likes_count = json_node['likes']['count']
		self.viewer_has_liked = json_node['likes'].get('viewer_has_liked', False)
		self.is_video = json_node['is_video']
		self.id = json_node['id']
		self.display_src = json_node['display_src']
		self.location = json_node['location']
		self.caption = json_node['caption']
		self.owner = User().from_json(json_node['owner'])

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
		self.username = json_node['username']
		self.full_name = json_node['full_name']
		self.profile_pic_url = json_node['profile_pic_url']
		self.is_unpublished = json_node['is_unpublished']
		self.blocked_by_viewer = json_node['blocked_by_viewer']
		self.id = json_node['id']
		self.is_private = json_node['is_private']

	def persist(self):
		pass
