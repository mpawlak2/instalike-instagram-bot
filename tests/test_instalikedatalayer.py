import json
from unittest import TestCase
from datalayer import InstalikeDataLayer, InstalikeSQLDAO
from model import Photo, User


class TestInstalikeDataLayer(TestCase):
    def create_test_user(self):
        return User().from_json(json.loads('{"connected_fb_page": null, "is_verified": false, "requested_by_viewer": false, "follows_viewer": false, "blocked_by_viewer": false, "followed_by": {"count": 286}, "external_url": null, "external_url_linkshimmed": null, "follows": {"count": 881}, "country_block": false, "followed_by_viewer": false, "media": {"nodes": [{"caption": "#selfie #polishboy #wis\u0142a #ski", "id": "1429264180820985541", "likes": {"count": 94}, "is_video": false, "date": 1484601589, "comments_disabled": false, "dimensions": {"width": 1080, "height": 1080}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/16110826_1082889121840788_5462237637802721280_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/16110826_1082889121840788_5462237637802721280_n.jpg", "comments": {"count": 1}, "__typename": "GraphImage", "code": "BPVxDMsBkbF", "owner": {"id": "2313248236"}}, {"caption": "#ksw37 #tauronarena #popek", "id": "1397476405285918942", "likes": {"count": 53}, "is_video": false, "date": 1480812191, "comments_disabled": false, "dimensions": {"width": 1080, "height": 1080}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/15337316_1837543259795123_7131108237918601216_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/15337316_1837543259795123_7131108237918601216_n.jpg", "comments": {"count": 1}, "__typename": "GraphImage", "code": "BNk1WLvDpje", "owner": {"id": "2313248236"}}, {"caption": "#krakow", "id": "1397208324508490613", "likes": {"count": 40}, "is_video": false, "date": 1480780233, "comments_disabled": false, "dimensions": {"width": 1080, "height": 1080}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/15258948_1831012847188178_4357902946436907008_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/15258948_1831012847188178_4357902946436907008_n.jpg", "comments": {"count": 0}, "__typename": "GraphImage", "code": "BNj4ZGDjBt1", "owner": {"id": "2313248236"}}, {"caption": "#warsaw #costam #staremiasto", "id": "1335769171615371303", "likes": {"count": 35}, "is_video": false, "date": 1473456115, "comments_disabled": false, "dimensions": {"width": 1080, "height": 1080}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/14309820_1729624990631170_1229190824_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/14309820_1729624990631170_1229190824_n.jpg", "comments": {"count": 0}, "__typename": "GraphImage", "code": "BKJmvwADVAn", "owner": {"id": "2313248236"}}, {"caption": "#sunglass #wall", "id": "1303534310133720189", "likes": {"count": 475}, "is_video": false, "date": 1469613420, "comments_disabled": false, "dimensions": {"width": 1080, "height": 1080}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/13707215_994359000662301_1486327023_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/13707215_994359000662301_1486327023_n.jpg", "comments": {"count": 2}, "__typename": "GraphImage", "code": "BIXFYx0DeR9", "owner": {"id": "2313248236"}}, {"caption": "#dirty #job", "id": "1270450070570046502", "likes": {"count": 817}, "is_video": false, "date": 1465669472, "comments_disabled": false, "dimensions": {"width": 1080, "height": 1050}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/13398695_1071735586238693_368272806_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/c15.0.1050.1050/13398695_1071735586238693_368272806_n.jpg", "comments": {"count": 1}, "__typename": "GraphImage", "code": "BGhi5upMpQm", "owner": {"id": "2313248236"}}, {"caption": "#night #benidorm #street", "id": "1257840608751556069", "likes": {"count": 705}, "is_video": false, "date": 1464166307, "comments_disabled": false, "dimensions": {"width": 1080, "height": 811}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/12093561_250277765330677_1139662062_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/c134.0.811.811/12093561_250277765330677_1139662062_n.jpg", "comments": {"count": 1}, "__typename": "GraphImage", "code": "BF0v16MspXl", "owner": {"id": "2313248236"}}, {"caption": "#beach #kebab", "id": "1252850660088648710", "likes": {"count": 800}, "is_video": false, "date": 1463571458, "comments_disabled": false, "dimensions": {"width": 1080, "height": 811}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/13259466_521638571376329_385240268_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/c134.0.811.811/13259466_521638571376329_385240268_n.jpg", "comments": {"count": 1}, "__typename": "GraphImage", "code": "BFjBQmXMpQG", "owner": {"id": "2313248236"}}, {"caption": "#bokeh", "id": "1242878538708850519", "likes": {"count": 472}, "is_video": false, "date": 1462382689, "comments_disabled": false, "dimensions": {"width": 1080, "height": 1080}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/13116560_235329563499663_720587766_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/13116560_235329563499663_720587766_n.jpg", "comments": {"count": 2}, "__typename": "GraphImage", "code": "BE_l3ImspdX", "owner": {"id": "2313248236"}}, {"id": "1139209619159291108", "likes": {"count": 505}, "is_video": false, "date": 1450024391, "comments_disabled": false, "dimensions": {"width": 1080, "height": 608}, "display_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/12331639_751410204965667_936218715_n.jpg", "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/c236.0.608.608/12331639_751410204965667_936218715_n.jpg", "owner": {"id": "2313248236"}, "__typename": "GraphImage", "code": "_PSRzispTk", "comments": {"count": 0}}], "page_info": {"has_next_page": false, "end_cursor": "AQDk42aTYA-kKnVGtF9etgfOo2d3mWFlbWptQIwfwFxlCXZfw9acaj6qacFwpulN9Sw"}, "count": 10}, "id": "2313248236", "biography": null, "has_blocked_viewer": false, "profile_pic_url": "https://scontent-waw1-1.cdninstagram.com/t51.2885-19/s150x150/15803271_221151991674584_3919420393634398208_a.jpg", "username": "mateusz5272", "is_private": false, "full_name": "Mateusz Pawlak", "profile_pic_url_hd": "https://scontent-waw1-1.cdninstagram.com/t51.2885-19/s320x320/15803271_221151991674584_3919420393634398208_a.jpg", "has_requested_viewer": false}'))

    def test_shouldNotInstantiateAbstractClass(self):
        exception = 0
        try:
            InstalikeDataLayer()
            self.fail('Instantiating InstalikeDataLayer should raise TypeError exception.')
        except TypeError:
            exception = 1

        if exception == 0:
            self.fail('Instantiating InstalikeDataLayer should raise TypeError exception.')

    def test_should_create_sqlite_dao(self):
        dao = InstalikeSQLDAO()
        self.assertIsNotNone(dao)

    def test_should_persist_photo(self):
        test_photo = Photo().from_json(json.loads('''
                            {"code": "tedwefeqwfa4s",
                            "dimensions": {"width": 1080, "height": 1349},
                            "comments_disabled": false,
                            "owner": {"id": "11111111"},
                            "comments": {"count": 134},
                            "caption": "#sunday#black#girl#selfie",
                            "likes": {"count": 12},
                            "date": 1476637330,
                            "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/whatever/whatever",
                            "is_video": false,
                            "id": "3333333333333333333",
                            "display_src": "https://scontent-waw1-1.cdninstagram.com/whatever/whatever"}'''))

        dao = InstalikeSQLDAO()
        rows = dao.persist_photo(test_photo)

        self.assertEqual(rows, 1)

    def test_should_persist_user(self):
        test_user = self.create_test_user()
        dao = InstalikeSQLDAO()
        rows = dao.persist_user(test_user)

        self.assertEqual(rows, 1)

    def test_should_persist_like(self):
        test_photo = Photo().from_json(json.loads('''
                            {"code": "tedwefeqwfa4s",
                            "dimensions": {"width": 1080, "height": 1349},
                            "comments_disabled": false,
                            "owner": {"id": "11111111"},
                            "comments": {"count": 134},
                            "caption": "#sunday#black#girl#selfie",
                            "likes": {"count": 12},
                            "date": 1476637330,
                            "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/whatever/whatever",
                            "is_video": false,
                            "id": "3333333333333333333",
                            "display_src": "https://scontent-waw1-1.cdninstagram.com/whatever/whatever"}'''))

        dao = InstalikeSQLDAO()
        rows = dao.persist_like(test_photo)

        self.assertEqual(rows, 1)

    def test_should_persist_follow(self):
        test_user = self.create_test_user()
        dao = InstalikeSQLDAO()

        rows = dao.persist_follow(test_user)

        self.assertEqual(rows, 1)

    def test_should_persist_unfollow(self):
        test_user = self.create_test_user()
        dao = InstalikeSQLDAO()
        rows = dao.persist_unfollow(test_user)

        self.assertEqual(rows, 1)

    def test_should_not_persist_unfollow_if_not_following(self):
        test_user = self.create_test_user()
        test_user.id = 2

        dao = InstalikeSQLDAO()
        rows = dao.persist_unfollow(test_user)

        self.assertEqual(rows, 0)

    def test_should_get_users_to_unfollow(self):
        dao = InstalikeSQLDAO()

        test_user = self.create_test_user()
        test_user.id = 4

        dao.persist_user(test_user)
        dao.persist_follow(test_user)

        rows = dao.get_users_to_unfollow(0)

        self.assertEqual(rows.count(), 1)

