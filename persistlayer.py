from abc import ABCMeta, abstractmethod


class PersistLayer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def merge_user(self, user_model):
        pass

    @abstractmethod
    def merge_photo(self, photo):
        pass

    @abstractmethod
    def persist_like(self, photo_model, status_code):
        pass

    @abstractmethod
    def persist_follow(self, user, status_code):
        pass

    @abstractmethod
    def persist_activity(self, activity):
        pass

    @abstractmethod
    def get_users_to_unfollow(self):
        pass

    @abstractmethod
    def update_unfollow_queue(self, days):
        pass

    @abstractmethod
    def persist_unfollow(self, user_id, status_code):
        pass