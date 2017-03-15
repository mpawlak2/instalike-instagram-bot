import unittest

from core.operation import Operations, Account


class TestAccount(unittest.TestCase):
    def test_create_account(self):
        acc = Account('user', 'pass')

        self.assertIsNotNone(acc)

    def test_return_json(self):
        acc = Account('user', 'pass')

        self.assertEqual(acc.to_json(), '{"username": "user", "password": "pass"}')

class TestOperations(unittest.TestCase):

    def test_create_operations_object(self):
        ops = Operations()

        self.assertIsNotNone(ops)

    def test_log_in(self):
        ops = Operations()

        self.assertTrue(ops.log_in())
