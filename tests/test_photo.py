from unittest import TestCase

from model import Photo
import json


class TestPhoto(TestCase):
    def test_should_not_create_photo_from_empty_json(self):
        test_photo = Photo().from_json(json.loads('{}'))
        self.assertTrue(test_photo == None)

    def test_should_not_create_photo_from_none(self):
        test_photo = Photo().from_json(None)
        self.assertTrue(test_photo == None)

    def test_should_create_photo_from_valid_json(self):
        test_photo = Photo().from_json(json.loads('''
                            {"code": "XxxXXxxXxxx",
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
        self.assertTrue(test_photo != None)
        self.assertTrue(test_photo.width == 1080)
        self.assertTrue(test_photo.height == 1349)
        self.assertTrue(test_photo.code == 'XxxXXxxXxxx')

    def test_should_not_create_photo_without_id(self):
        test_photo = Photo().from_json(json.loads('''
                                {"code": "XxxXXxxXxxx",
                                "dimensions": {"width": 1080, "height": 1349},
                                "comments_disabled": false,
                                "owner": {"id": "11111111"},
                                "comments": {"count": 134},
                                "caption": "#sunday#black#girl#selfie",
                                "likes": {"count": 12},
                                "date": 1476637330,
                                "thumbnail_src": "https://scontent-waw1-1.cdninstagram.com/whatever/whatever",
                                "is_video": false,
                                "id": "",
                                "display_src": "https://scontent-waw1-1.cdninstagram.com/whatever/whatever"}'''))
        self.assertTrue(test_photo == None)
