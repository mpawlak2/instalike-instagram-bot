import unittest

from core.operation import Operations


class TestOperations(unittest.TestCase):

    def test_create_operations_class(self):
        ops = Operations()

        self.assertIsNotNone(ops)