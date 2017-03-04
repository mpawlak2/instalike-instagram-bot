from unittest import TestCase

from logger.clogger import CLogger


class TestLogger(TestCase):
    def test_shouldInstantiateLogger(self):
        logger = CLogger()
        self.assertIsNotNone(logger)