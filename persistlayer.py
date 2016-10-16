from abc import ABCMeta, abstractmethod


class PersistLayer:
    __metaclass__ = ABCMeta

    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def merge_user(self, user_model):
        """Persist user in some way."""
        raise NotImplementedError

    @abstractmethod
    def merge_photo(self, photo):
        raise NotImplementedError

    @abstractmethod
    def persist_like(self, photo_model, status_code):
        raise NotImplementedError

    @abstractmethod
    def persist_follow(self, user, status_code):
        raise NotImplementedError

    @abstractmethod
    def persist_activity(self, activity):
        raise NotImplementedError

    @abstractmethod
    def get_users_to_unfollow(self):
        raise NotImplementedError

    @abstractmethod
    def update_unfollow_queue(self, days):
        raise NotImplementedError

    @abstractmethod
    def persist_unfollow(self, user_id, status_code):
        raise NotImplementedError