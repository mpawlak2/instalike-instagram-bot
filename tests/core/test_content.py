from unittest import TestCase

from core.content import ContentManager


class TestContent(TestCase):
    def test_create_class(self):
        test_content = ContentManager()

        self.assertIsNotNone(test_content)
