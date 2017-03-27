from types import GeneratorType
from unittest import TestCase

from core.content import ContentManager, TagMediaAlgorithm
from core.operation import Operations, Account


class TestContent(TestCase):
    def test_create_class(self):
        test_content = ContentManager()

        self.assertIsNotNone(test_content)

    def test_return_media_generator(self):
        test_content = ContentManager()
        gnt = test_content.get_media_generator()

        self.assertIsInstance(gnt, GeneratorType)

    def test_get_media_from_tag_algorithm(self):
        ops = Operations()
        ops.log_in(Account('alojzykk', '1q@W3e$R'))
        tma = TagMediaAlgorithm(['polishgirl', 'l4l'], ops)

        self.assertIsNotNone(tma.get_media())
