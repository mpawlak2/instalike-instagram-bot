from unittest import TestCase

from logger.clogger import CLogger


class TestLogger(TestCase):
    def test_shouldInstantiateLogger(self):
        logger = CLogger()
        logger.log('test mmiaisdf')
        fasdf

        self.assertIsNotNone(logger)