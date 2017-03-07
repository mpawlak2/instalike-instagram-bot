from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('instalike.db')

        def __init__(self):
            self.database.connect()


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