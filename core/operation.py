import hashlib
import json

import requests
import logging


API_URL = 'https://i.instagram.com/api/v1'
CONTENT_TYPE = 'application/x-www-form-urlencoded'
USER_AGENT = 'Instagram 10.3.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)'




class Account:
    csrftoken = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return json.dumps({'username': self.username, 'password': self.password})


class Operations:
    account = None
    response = None

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

    def get_csrftoken(self):
        self.send_request(API_URL + '/si/fetch_headers/')

        return self.response.cookies

    def generate_device_id(self, seed):
        volatile_seed = '12345'
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    def send_request(self, url, account=None, post_data=None):
        self.session.headers.update({
            'Connection': 'close',
            'User-Agent': USER_AGENT,
            'Accept': '*/*',
            'Content-Type': CONTENT_TYPE,
            'Accept-Language': 'en-US'
        })

        try:
            if post_data is not None:
                response = self.session.post(url, data=post_data)
            else:
                response = self.session.get(url)
        except Exception as e:
            logging.error(str(e))
            return None

        if response.status_code == 200:
            self.response = response
        else:
            self.response = None
            logging.warning('{0} request responded with status code {1}'.format('POST' if post_data is not None else 'GET', response.status_code))
            return None

        return response


