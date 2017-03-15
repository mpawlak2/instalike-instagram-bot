class TestConfiguration:
    def __init__(self):
        self.configuration_file = ''
        self.validated = True

    def initialize(self):
        self.instagram_username = 'username'
        self.instagram_password = 'password'

        # BOT SECTION
        self.bot_work_whole_time = False
        self.bot_work_at_day = False
        self.bot_stop_after_minutes = 0
        self.bot_work_hours = 6
        self.enable_instalike = True
        self.enable_instafollow = True
        self.enable_instacomment = False
        self.enable_instamessage = False
        self.botting_start_hour = 7
        self.botting_end_hour = 23
        self.log_db_operations = False

        # NOTIFICATIONS SECTION
        self.notification_enable_email = False
        self.notification_send_attachment = False
        self.notification_email_address = False

        # BAN SECTION
        self.avoid_bans = False

        # DATABASE
        self.enable_database = False
        self.database_name = 'instamanager'
        self.database_user = 'username'
        self.database_password = 'password'
        self.database_address = 'localhost'

        # INSTALIKE
        self.instalike_max_likes_per_hour = 200
        self.instalike_like_feed = False
        self.instalike_tags = 'tag, tag2, tag3'

        # INSTAFOLLOW
        self.instafollow_max_follows_per_hour = 8
        self.instafollow_max_unfollows_per_hour = 2
        self.instafollow_unfollow_users = False
        self.instafollow_unfollow_after_days = 6

        # BLACKLIST
        self.banned_tags = 'tagss, tag23'
        self.banned_words_in_user_desc = 'dupa'
        self.username_blacklist = []

        # LIKEFILTER
        self.like_min_likes_on_photo = 0
        self.like_max_likes_on_photo = 0

        if (not self.banned_tags):
            self.banned_tags = []
        else:
            self.banned_tags = list(map(lambda tag: '#' + tag.strip(), self.banned_tags.split(',')))

        if (len(self.username_blacklist) > 0):
            self.username_blacklist = list(map(lambda username: username.strip(), self.username_blacklist.split(',')))

        if (not self.banned_words_in_user_desc):
            self.banned_words_in_user_desc = []
        else:
            self.banned_words_in_user_desc = list(
                map(lambda tag: tag.strip(), self.banned_words_in_user_desc.split(',')))

        if (self.instafollow_max_unfollows_per_hour <= 0):
            self.instafollow_max_unfollows_per_hour = 1
            self.instafollow_unfollow_users = False

        return True

    def validate(self):
        return True