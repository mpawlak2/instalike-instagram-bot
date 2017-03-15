import json


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return json.dumps({'username': self.username, 'password': self.password})

class Operations:
    def log_in(self, account):
        pass

    def log_out(self, account):
        pass

    def like_media(self, photo_id):
        pass

    def unlike_media(self, photo_id):
        pass

    def follow_user(self, user_id):
        pass

    def unfollow_user(self, user_id):
        pass

    def comment_media(self, media_id):
        pass

    def block_user(self, user_id):
        pass

    def send_direct_message(self, user_id, message):
        pass
