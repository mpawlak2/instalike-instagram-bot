from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('instalike.db')


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
