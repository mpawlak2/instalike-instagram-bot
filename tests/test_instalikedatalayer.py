import json
from unittest import TestCase
from datalayer import InstalikeDataLayer, InstalikeSQLDAO
from model import Photo


class TestInstalikeDataLayer(TestCase):
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

