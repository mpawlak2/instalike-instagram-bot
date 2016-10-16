from unittest import TestCase

from persistlayer import PersistLayer


class TestPersist(TestCase):
    def test_shouldNotInstantiateAbstractClass(self):
        self.assertRaises(NotImplementedError, PersistLayer)
