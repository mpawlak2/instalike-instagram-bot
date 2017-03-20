import json
import unittest

import logging

from core.operation import Operations, Account

logging.basicConfig(level=logging.DEBUG)

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

        self.assertTrue(ops.log_in(Account('alojzykk', '1q@W3e$R')))
        self.assertTrue(ops.log_in())

    def test_log_in_fail(self):
        ops = Operations()

        self.assertFalse(ops.log_in(Account('fakeacc', 'fakepass')))

    def test_account_assignment(self):
        ops = Operations()

        self.assertFalse(ops.log_in())
        self.assertFalse(ops.log_in())
        self.assertIsNone(ops.account)

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

        self.assertIsNotNone(acc.get_phone_id())


    def test_guid(self):
        acc = Account('testacc', 'testpass')

        self.assertIsNotNone(acc.get_guid())

    def test_logout(self):
        ops = Operations()

        self.assertTrue(ops.log_in(Account('alojzykk', '1q@W3e$R')))
        self.assertTrue(ops.log_out())
        self.assertTrue(ops.log_in())

    def test_get_media_from_tag(self):
        ops = Operations()
        ops.log_in(Account('alojzykk', '1q@W3e$R'))

        self.assertIsNotNone(ops.get_media_by_tag('polishgirl'))
        self.assertIsNotNone(json.dumps(ops.get_media_by_tag('polishgirl')))
