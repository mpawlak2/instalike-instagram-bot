import requests
import re
import json


class Operations:
    # url's
    base_url = 'https://www.instagram.com/'
    login_url = 'https://www.instagram.com/accounts/login/?force_classic_login&hl=pl'
    post_ajx_login_url = 'https://www.instagram.com/accounts/login/ajax/'
    logout_url = 'https://www.instagram.com/accounts/logout/'  # requires csrfmiddlewaretoken as payload
    like_url_tmpl = 'https://www.instagram.com/web/likes/{0}/like/'
    unlike_url_tmpl = 'https://www.instagram.com/web/likes/{0}/unlike/'
    follow_url_tmpl = 'https://www.instagram.com/web/friendships/{0}/follow/'
    unfollow_url_tmpl = 'https://www.instagram.com/web/friendships/{0}/unfollow/'
    comment_url_tmpl = 'https://www.instagram.com/web/comments/{0}/add/'  # payload = { comment_text : 'wow'}
    tag_url = 'https://www.instagram.com/explore/tags/{0}/?__a=1'
    photo_details_url_tmpl = 'https://www.instagram.com/p/{0}/?__a=1'  # in {0} goes the image code GET __a=1 - return only json
    user_details_url_tmpl = 'https://www.instagram.com/{0}/?__a=1'  # user name as uid
    get_account_activity_url = 'https://www.instagram.com/accounts/activity/?__a=1'

    # info
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    accept_language = 'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4'
    content_type = 'application/x-www-form-urlencoded'

    session = requests.Session()
    pending_error = False

    headers = dict()
    ajx_headers = dict()
    cookies = dict()

    def log_in(self, username, password):
        payload = {
            'username': username,
            'password': password
        }

        # get unique csrftoken from server
        response = self.session.get(self.base_url)
        if (response.status_code != 200):
            print('code: {0}, could not GET: {1}'.format(response.status_code, self.base_url))
            return None

        self.prepare_request(response)
        response = self.session.post(self.post_ajx_login_url, data=payload, headers=self.ajx_headers,
                                     cookies=response.cookies)
        if (response.status_code != 200):
            print('code: {0}, could not POST: {1}'.format(response.status_code, self.login_url))
            return None
        # update csrftoken
        self.prepare_request(response)

        is_logged = json.loads(response.content.decode('utf-8'))['authenticated']
        if (not is_logged):
            print(
                'Check credentials, also try to log in to your account manually to check if everything is fine then retry.')
            return None
        self.cookies = response.cookies

        return response

    def log_out(self):
        return self.session.post(self.logout_url, headers=self.headers, cookies=self.cookies)

    def is_logged_in(self):
        pass

    def has_error(self):
        return self.pending_error

    def clear_error(self):
        self.pending_error = False

    # dont use
    def prepare_ajax_request(self, request_response):
        self.ajx_headers = {
            'origin': self.base_url,
            'referer': request_response.url,
            'User-Agent': self.user_agent,
            'content-type': self.content_type,
            'accept-language': self.accept_language,
            'accept-encoding': 'gzip, deflate',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'x-csrftoken': request_response.cookies['csrftoken'],
            'x-instagram-ajax': '1',
            'x-request-with': 'XMLHttpRequest'
        }

    # dont use
    def prepare_request(self, request_response):
        self.headers = {
            'origin': self.base_url,
            'referer': request_response.url,
            'User-Agent': self.user_agent,
            'content-type': self.content_type,
            'accept-language': self.accept_language,
            'accept-encoding': 'gzip, deflate',
            'x-csrftoken': request_response.cookies['csrftoken'],
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

        self.cookies = request_response.cookies
        self.prepare_ajax_request(request_response)

    def like(self, photo_id):
        response = None
        try:
            response = self.session.post(self.like_url_tmpl.format(photo_id), headers=self.ajx_headers,
                                         cookies=self.cookies)
        except requests.exceptions.ConnectionError:
            pending_error = True
        return response

    def like_media(self, media):
        response = None
        try:
            response = self.session.post(self.like_url_tmpl.format(media.get_id()), headers=self.ajx_headers,
                                         cookies=self.cookies)
            if (response.status_code != 200):
                print('code: {0}, could not POST {1}'.format(response.status_code,
                                                             self.like_url_tmpl.format(media.get_id())))
                return None
        except requests.exceptions.ConnectionError:
            pending_error = True
        return response

    def unlike(self, photo_id):
        return self.session.post(self.unlike_url_tmpl.format(photo_id), headers=self.ajx_headers, cookies=self.cookies)

    def follow(self, user_id):
        response = self.session.post(self.follow_url_tmpl.format(user_id), headers=self.ajx_headers,
                                     cookies=self.cookies)
        return response

    def unfollow(self, user_id):
        return self.session.post(self.unfollow_url_tmpl.format(user_id), headers=self.ajx_headers, cookies=self.cookies)

    def comment_photo(self, photo_id, comment):
        payload = {
            'comment_text': comment
        }

        return self.session.post(self.comment_url_tmpl.format(photo_id), data=payload, headers=self.ajx_headers,
                                 cookies=self.cookies)

    def delete_my_comment(self, photo_id, comment_id):
        pass

    def delete_comment_uden_my_photo(self, photo_id, comment_id):
        pass

    def get_photos_by_tag(self, tag):
        response = self.session.get(self.tag_url.format(tag), headers=self.headers)
        if (response.status_code != 200):
            return None

        return json.loads(response.content.decode('utf-8'))['tag']['media']['nodes']

    def get_feed_media(self):
        response = self.session.get(self.base_url, headers=self.headers)
        if (response.status_code != 200):
            return None

        # Find feed media in html file.
        feed_media = re.search('window._sharedData = ({.*});', response.content.decode('utf-8'))
        if (feed_media):
            json_feed = \
            json.loads(feed_media.group(1))['entry_data']['FeedPage'][0]['graphql']['user']['edge_web_feed_timeline'][
                'edges']
            return json_feed
        return None

    def get_activity(self):
        response = self.session.get(self.get_account_activity_url, headers=self.headers)

        if (response.status_code != 200):
            return None

        try:
            decoded = json.loads(response.content.decode('utf-8'))
        except json.decoder.JSONDecodeError:
            return None

        activityFeed = decoded.get('activityFeed', None)
        if (not activityFeed):
            return None

        return activityFeed.get('stories', None)

    def get_photo_details(self, photo_code):
        response = self.session.get(self.photo_details_url_tmpl.format(photo_code), headers=self.headers)

        if (response.status_code != 200):
            return None
        return json.loads(response.content.decode('utf-8'))['media']

    def get_user_details(self, user_name):
        response = self.session.get(self.user_details_url_tmpl.format(user_name), headers=self.headers)

        if (response.status_code != 200):
            return None
        return json.loads(response.content.decode('utf-8'))['user']

    def get_my_followers(self):
        pass

    def get_my_following(self):
        pass

    def get_user_followers(self, user_id):
        pass

    def get_user_following(self, user_id):
        pass

    def block_user(self, user_id):
        pass
