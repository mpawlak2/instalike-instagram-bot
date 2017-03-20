import hashlib
import json

import requests
import logging
import uuid
import hmac

API_URL = 'https://i.instagram.com/api/v1'
CONTENT_TYPE = 'application/x-www-form-urlencoded'
USER_AGENT = 'Instagram 9.2.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)'
PRIVATE_KEY = '012a54f51c49aa8c5c322416ab1410909add32c966bbaa0fe3dc58ac43fd7ede'



class Account:
    csrftoken = None
    __phone_id = None
    __device_id = None
    __guid = None
    logged_in = False

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        return json.dumps({'username': self.username, 'password': self.password})

    def get_login_data(self):
        return json.dumps({
            'phone_id': self.get_phone_id(),
            '_csrftoken': self.csrftoken,
            'username': self.username,
            'password': self.password,
            'device_id': self.get_device_id(),
            'guid': self.get_guid(),
            'login_attempt_count': '0'
        })

    def get_phone_id(self, no_dash=False):
        if self.__phone_id is None:
            self.__phone_id = str(uuid.uuid4())
            logging.info('generated phone id: {0}'.format(self.__phone_id))
        return self.__phone_id if not no_dash else self.__phone_id.replace('-', '')

    def get_device_id(self):
        if self.__device_id is None:
            m = hashlib.md5()
            m.update(self.username.encode('utf-8'))
            user_seed = m.hexdigest()
            m.update('0192837465'.encode('utf-8') + user_seed.encode('utf-8'))
            self.__device_id = 'android-' + m.hexdigest()[:16]
            logging.info('generated device id: {0}'.format(self.__device_id))

        return self.__device_id

    def get_guid(self):
        if self.__guid is None:
            self.__guid = str(uuid.uuid4())
        return self.__guid


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

        # Already logged in.
        if self.account.logged_in:
            return True

        if self.account.csrftoken is None:
            self.account.csrftoken = self.get_csrftoken()

        # could not get csrftoken
        if self.account.csrftoken is None:
            return False

        if self.send_request(API_URL + '/accounts/login/', post_data=self.sign_payload(self.account.get_login_data())):
            self.account.logged_in = True
            logging.info('logged in successfully as {0}'.format(self.account.username))
            return True

        return False

    def log_out(self):
        if not self.account.logged_in:
            return True

        return self.send_request(API_URL + '/accounts/logout/')

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

    def get_media_by_tag(self, tag):
        pass

    def get_media_from_feed(self):
        pass

    def get_csrftoken(self):
        return self.send_request(API_URL + '/si/fetch_headers/').cookies['csrftoken']

    def send_request(self, url, post_data=None):
        logging.info('sending request ' + url)
        self.session.headers.update({
            'Connection': 'close',
            'Cookie2': '$Version=1',
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
            logging.warning('{0} request responded with status code: {1}, content: {2}'.format('POST' if post_data is not None else 'GET', response.status_code, response.text))
            return None

        try:
            json.loads(response.text)
        except Exception as e:
            logging.debug('response content is not in JSON format, response: {0}, exception: {1}', response.text, str(e))

        return self.response

    def sign_payload(self, payload):
        signed_payload = 'ig_sig_key_version=4&signed_body=' + hmac.new(PRIVATE_KEY.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest() + '.' + payload
        logging.debug('signed payload: ' + signed_payload)
        return signed_payload


