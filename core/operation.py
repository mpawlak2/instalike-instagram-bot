import json

import requests

API_URL = 'https://i.instagram.com/api/v1'


class Account:
    csrftoken = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return json.dumps({'username': self.username, 'password': self.password})


class Operations:
    account = None

    def __init__(self):
        self.session = requests.Session()

    def log_in(self, account=None):
        if account is None:
            if self.account is None:
                return False
        else:
            self.account = account

        if self.account.csrftoken is None:
            self.account.csrftoken = self.get_csrftoken()

        # could not get csrftoken
        if self.account.csrftoken is None:
            return False

        return True

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

    # Instagram API
    def get_csrftoken(self):
        try:
            response = requests.get(API_URL + '/si/fetch_headers/')
        except Exception as e:
            return None

        return response.cookies

    def send_request(self, url):
        pass
