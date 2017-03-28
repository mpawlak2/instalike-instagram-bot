import datetime
from abc import ABC, abstractmethod


class MediaAlgorithm(ABC):
    @abstractmethod
    def get_media(self):
        pass


class TagMediaAlgorithm(MediaAlgorithm):
    __tag_list = []
    __operations = None

    def __init__(self, tag_list, operations):
        self.__tag_list = tag_list
        self.__operations = operations

    def get_media(self):
        media_list = []

        tag = self.__tag_list.pop()
        self.__tag_list.append(tag)

        media_json = self.__operations.get_media_by_tag(tag)
        for media in media_json['items']:
            media_list.append(media)

        return media_list


class FeedMediaAlgorithm(MediaAlgorithm):
    __operations = None

    def __init__(self, operations):
        self.__operations = operations

    def get_media(self):
        media_list = []

        media_json = self.__operations.get_media_from_feed()

        for media in media_json['items']:
            media_list.append(media)

        return media_list


class ContentManager:
    __media_list = []
    __media_algorithm = None
    __media_generator = None
    __media_update_date = datetime.datetime.today()

    def get_next_media(self):
        if self.__media_generator is None:
            self.__media_generator = self.get_media_generator()

        return next(self.__media_generator)

    def get_media_generator(self):
        if not self.__media_list or (datetime.datetime.today() - self.__media_update_date).total_seconds() > 2 * 60:
            self.download_media()

        yield self.__media_list.pop()

    def download_media(self):
        self.__media_list = self.__media_algorithm.get_media()
        self.__media_update_date = datetime.datetime.today()


class Validator:
    __banned_usernames = []
    __banned_tags = []

    # MEDIA VALIDATION
    min_likes = 0
    max_likes = 0
    min_comments = 0
    max_comments = 0
    max_days_old = 0
    spam_media_words = []  # look for these words in description, if found media is not valid.

    # USER VALIDATOIN
    min_followers = 0
    max_followers = 0
    min_posts = 0
    max_posts = 0
    max_days_last_post = 0
    spam_user_words = []

    def validate_users(self, user_list):
        pass

    def validate_media(self, media_list):
        pass
