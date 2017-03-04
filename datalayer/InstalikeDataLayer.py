from abc import ABC, abstractmethod

import model

""" If you wish to have new persistence plugin - implement these methods. """
class InstalikeDataLayer(ABC):
    @abstractmethod
    def persist_user(self, user: model.User):
        pass

    @abstractmethod
    def persist_photo(self, photo: model.Photo):
        pass

    @abstractmethod
    def persist_like(self, photo: model.Photo):
        pass

    @abstractmethod
    def persist_follow(self, user: model.User):
        pass

    @abstractmethod
    def persist_unfollow(self, user: model.User):
        pass

    @abstractmethod
    def persist_activity(self, activity: model.Activity):
        pass

    @abstractmethod
    def get_users_to_unfollow(self, day_range):
        pass


