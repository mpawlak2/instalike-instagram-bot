import json
import unittest

from core.operation import Operations, Account


class TestAccount(unittest.TestCase):
    def test_create_account(self):
        acc = Account('user', 'pass')

        self.assertIsNotNone(acc)

    def test_return_json(self):
        acc = Account('user', 'pass')

        self.assertEqual(acc.to_json(), json.dumps({'username': 'user', 'password': 'pass'}))

class TestOperations(unittest.TestCase):

    def test_create_operations_object(self):
        ops = Operations()

        self.assertIsNotNone(ops)

    def test_log_in(self):
        ops = Operations()

        self.assertTrue(ops.log_in(Account('user', 'password')))

    def test_log_in_fail(self):
        ops = Operations()

        self.assertFalse(ops.log_in(Account('fakeacc', 'fakepass')))

    def test_account_assignment(self):
        ops = Operations()

        self.assertFalse(ops.log_in())
        self.assertIsNone(ops.account)
        self.assertTrue(ops.log_in(Account('legitacc', 'legitpass')))
        self.assertIsNotNone(ops.account)

    def test_get_csrftoken(self):
        ops = Operations()
        ops.log_in(Account('fake', 'fake'))

        self.assertIsNotNone(ops.account.csrftoken)
        self.assertIsNotNone(ops.get_csrftoken())

    def test_send_request_get(self):
        ops = Operations()

        self.assertIsNotNone(ops.send_request('https://i.instagram.com/api/v1/si/fetch_headers/'))
        self.assertIsNotNone(ops.response)

    def test_device_id(self):
        acc = Account('testacc', 'testpass')

        # should return same device id when same username.
        device_id = acc.get_device_id()
        acc.__device_id = None
        self.assertEqual(device_id, acc.get_device_id())

    def test_phone_id(self):
        acc = Account('testacc', 'testpass')

        print(acc.get_phone_id())


    def test_guid(self):
        acc = Account('testacc', 'testpass')

        self.assertIsNotNone(acc.get_guid())

