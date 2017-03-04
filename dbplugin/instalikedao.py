import model
from datalayer.InstalikeDataLayer import InstalikeDataLayer


class InstalikeDAO(InstalikeDataLayer):
    def set_datasource(self, datasource):
        self.datasource = datasource

    def persist_activity(self, activity: model.Activity):
        pass

    def persist_user(self, user: model.User):
        pass

    def get_users_to_unfollow(self, day_range):
        pass

    def persist_like(self, photo: model.Photo):
        pass

    def persist_follow(self, user: model.User):
        pass

    def persist_photo(self, photo: model.Photo):
        pass

    def persist_unfollow(self, user: model.User):
        pass

