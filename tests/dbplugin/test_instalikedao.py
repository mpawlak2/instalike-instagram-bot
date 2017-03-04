from unittest import TestCase

from dbplugin.instalikedao import InstalikeDAO


class TestInstalikeDAO(TestCase):
    def test_classInstalikeDAOImplementsAllMethods(self):
        try:
            object = InstalikeDAO()
        except TypeError:
            self.fail('Error instantiating InstalikeDAO class.')

