from persistlayer import PersistLayer


class Repository(PersistLayer):
    def __init__(self):
        pass

    def update_unfollow_queue(self, days):
        pass

    def persist_unfollow(self, user_id, status_code):
        pass

    def persist_follow(self, user, status_code):
        pass

    def persist_like(self, photo_model, status_code):
        pass

    def get_users_to_unfollow(self):
        pass

    def merge_user(self, user_model):
        pass

    def persist_activity(self, activity):
        pass

    def merge_photo(self, photo):
        pass

