from peewee import *
import model
from abc import ABC, abstractmethod

# SQLite database connection
sqlite_db = SqliteDatabase('instalike.db')

""" If you wish to have new persistence plugin derive from this class and implement these methods. """


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
    def get_users_to_unfollow(self, day_range):
        pass


class InstalikeSQLDAO(InstalikeDataLayer):
    def __init__(self):
        sqlite_db.connect()

    def persist_user(self, user: model.User):
        sql_query = '''select merge_user(
        						_id := {0},
        						_username := {1},
        						_has_blocked_viewer := {2},
        						_follows_count := {3},
        						_followed_by_count := {4},
        						_external_url := {5},
        						_follows_viewer := {6},
        						_profile_pic_url := {7},
        						_is_private := {8},
        						_full_name := {9},
        						_posts_count := {10},
        						_blocked_by_viewer := {11},
        						_followed_by_viewer := {12},
        						_is_verified := {13},
        						_biography := {14})'''
        sql_query = sql_query.format(
            user.id,
            user.username,
            user.has_blocked_viewer,
            user.follows_count,
            user.followed_by_count,
            user.external_url,
            user.follows_viewer,
            user.profile_pic_url,
            user.is_private,
            user.full_name,
            user.posts_count,
            user.blocked_by_viewer,
            user.followed_by_viewer,
            user.is_verified,
            user.biography)

        self.data_source.get_connection().get_connection().execute(sql_query)

    def get_users_to_unfollow(self, day_range):
        pass

    def persist_like(self, photo: model.Photo):
        sql_query = 'select like_photo(_photo_id := {0}, _status_code := 200)'
        sql_query = sql_query.format(photo.id)

        self.data_source.get_connection().execute(sql_query)

    def persist_follow(self, user: model.User):
        sql_query = 'select follow_user(_user_id := {0}, _status_code := 200)'
        sql_query = sql_query.format(user.id)

        self.data_source.get_connection().execute(sql_query)

    def persist_photo(self, photo: model.Photo):
        if Photo.select().where(Photo.code == photo.code).exists():
            photo_model = Photo.get(Photo.code == photo.code)
        else:
            photo_model = Photo(width = photo.width,
                            height = photo.height,
                            code = photo.code,
                            is_ad = photo.is_ad,
                            likes_count = photo.likes_count,
                            viewer_has_liked = photo.viewer_has_liked,
                            is_video = photo.is_video,
                            display_src = photo.display_src,
                            location = photo.location)

        photo_model.save()

    def persist_unfollow(self, user: model.User):
        sql_query = 'select unfollow(_user_id := {0}, _status_code := 200)'.format(user.id)

        self.data_source.get_connection().execute(sql_query)


# Model Definitions

class BaseModel(Model):
    class Meta:
        database = sqlite_db


class Photo(BaseModel):
    width = IntegerField()
    height = IntegerField()
    code = CharField()
    is_ad = BooleanField()
    likes_count = IntegerField()
    viewer_has_liked = BooleanField()
    is_video = BooleanField()
    display_src = CharField()
    location = CharField()
    owner_id = IntegerField()
    caption = CharField()
    owner_name = CharField()


class User(BaseModel):
    name = CharField()
    has_blocked_viewer = BooleanField()
    follows_count = IntegerField()
    followers_count = IntegerField()
    external_url = CharField()
    follows_viewer = BooleanField()
    profile_pic_url = CharField()
    is_private = BooleanField()
    full_name = CharField()
    posts_count = IntegerField()
    blocked_by_viewer = BooleanField()
    followed_by_viewer = BooleanField()
    is_verified = BooleanField()
    biography = CharField()
