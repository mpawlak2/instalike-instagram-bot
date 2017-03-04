from unittest import TestCase

from datalayer.InstalikeDataLayer import InstalikeDataLayer


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

