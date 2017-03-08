import datetime
from peewee import *
import model
from abc import ABC, abstractmethod

# SQLite database connection
sqlite_db = SqliteDatabase('instalike.db')
sqlite_db.connect()
recreate_tables = True


# Model Definitions
class BaseModel(Model):
    class Meta:
        database = sqlite_db


class Photo(BaseModel):
    id = IntegerField(primary_key=True)
    width = IntegerField()
    height = IntegerField()
    code = CharField()
    is_ad = BooleanField(null=True)
    likes_count = IntegerField()
    viewer_has_liked = BooleanField(null=True)
    is_video = BooleanField(null=True)
    display_src = CharField(null=True)
    location = CharField(null=True)
    owner_id = IntegerField(null=True)
    caption = CharField(null=True)
    owner_name = CharField(null=True)
    creation_date = DateTimeField()
    mod_date = DateTimeField()


class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    has_blocked_viewer = BooleanField(null=True)
    follows_count = IntegerField()
    followers_count = IntegerField()
    external_url = CharField(null=True)
    follows_viewer = BooleanField()
    profile_pic_url = CharField(null=True)
    is_private = BooleanField()
    full_name = CharField(null=True)
    posts_count = IntegerField()
    blocked_by_viewer = BooleanField()
    followed_by_viewer = BooleanField()
    is_verified = BooleanField(null=True)
    biography = CharField(null=True)
    creation_date = DateTimeField()
    mod_date = DateTimeField()


class Like(BaseModel):
    id = PrimaryKeyField()
    photo_id = IntegerField()
    event_time = DateTimeField()


class Follow(BaseModel):
    id = PrimaryKeyField()
    user_id = IntegerField()
    event_time = DateTimeField()


if recreate_tables:
    if Photo.table_exists():
        Photo.drop_table()
    if User.table_exists():
        User.drop_table()
    if Like.table_exists():
        Like.drop_table()
    if Follow.table_exists():
        Follow.drop_table()

if not Photo.table_exists():
    Photo.create_table()

if not User.table_exists():
    User.create_table()

if not Like.table_exists():
    Like.create_table()

if not Follow.table_exists():
    Follow.create_table()

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
    def persist_user(self, user: model.User):
        update = False
        if User.select().where(User.id == user.id).exists():
            update = True
            user_model = User.get(User.id == user.id)

            user_model.name = user.username
            user_model.has_blocked_viewer = user.has_blocked_viewer
            user_model.follows_count = user.follows_count
            user_model.followers_count = user.followed_by_count
            user_model.external_url = user.external_url
            user_model.follows_viewer = user.follows_viewer
            user_model.profile_pic_url = user.profile_pic_url
            user_model.is_private = user.is_private
            user_model.full_name = user.full_name
            user_model.posts_count = user.posts_count
            user_model.blocked_by_viewer = user.blocked_by_viewer
            user_model.followed_by_viewer = user.followed_by_viewer
            user_model.is_verified = user.is_verified
            user_model.biography = user.biograph
        else:
            user_model = User(id=user.id,
                              name=user.username,
                              has_blocked_viewer=user.has_blocked_viewer,
                              follows_count=user.follows_count,
                              followers_count=user.followed_by_count,
                              external_url=user.external_url,
                              follows_viewer=user.follows_viewer,
                              profile_pic_url=user.profile_pic_url,
                              is_private=user.is_private,
                              full_name=user.full_name,
                              posts_count=user.posts_count,
                              blocked_by_viewer=user.blocked_by_viewer,
                              followed_by_viewer=user.followed_by_viewer,
                              is_verified=user.is_verified,
                              biography=user.biography,
                              creation_date=datetime.datetime.today())

        user_model.mod_date = datetime.datetime.today()

        return user_model.save() if update else user_model.save(force_insert=True)

    def get_users_to_unfollow(self, day_range):
        pass

    def persist_like(self, photo: model.Photo):
        like_model = Like(photo_id=photo.id, event_time=datetime.datetime.today())

        return like_model.save()

    def persist_follow(self, user: model.User):
        follow_model = Follow(user_id = user.id, event_time = datetime.datetime.today())

        return follow_model.save()

    def persist_photo(self, photo: model.Photo):
        update = False
        if Photo.select().where(Photo.id == photo.id).exists():
            update = True
            photo_model = Photo.get(Photo.id == photo.id)

            photo_model.width = photo.width
            photo_model.height = photo.height
            photo_model.is_ad = photo.is_ad
            photo_model.likes_count = photo.likes_count
            photo_model.viewer_has_like = photo.viewer_has_liked
            photo_model.is_video = photo.is_video
            photo_model.display_src = photo.display_src
            photo_model.location = photo.location
        else:
            photo_model = Photo(id=photo.id,
                                width=photo.width,
                                height=photo.height,
                                code=photo.code,
                                is_ad=photo.is_ad,
                                likes_count=photo.likes_count,
                                viewer_has_liked=photo.viewer_has_liked,
                                is_video=photo.is_video,
                                display_src=photo.display_src,
                                location=photo.location,
                                creation_date=datetime.datetime.today())

        photo_model.mod_date = datetime.datetime.today()

        return photo_model.save() if update else photo_model.save(force_insert=True)

    def persist_unfollow(self, user: model.User):
        sql_query = 'select unfollow(_user_id := {0}, _status_code := 200)'.format(user.id)

        self.data_source.get_connection().execute(sql_query)
