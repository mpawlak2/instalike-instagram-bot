import model
from datalayer.InstalikeDataLayer import InstalikeDataLayer


class InstalikeDAO(InstalikeDataLayer):
    def set_datasource(self, datasource):
        self.datasource = datasource

    def persist_activity(self, activity: model.Activity):
        pass

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

        self.datasource.execute(sql_query)

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
