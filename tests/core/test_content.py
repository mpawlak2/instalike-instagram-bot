from types import GeneratorType
from unittest import TestCase

from core.content import ContentManager


class TestContent(TestCase):
    def test_create_class(self):
        test_content = ContentManager()

        self.assertIsNotNone(test_content)

    def test_return_media_generator(self):
        test_content = ContentManager()
        gnt = test_content.get_media_generator()

        self.assertIsInstance(gnt, GeneratorType)
