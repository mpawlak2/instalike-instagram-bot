from unittest import TestCase

from dbplugin.pgdatasource import PGDataSource
from dbplugin.instalikedao import InstalikeDAO


class TestInstalikeDAO(TestCase):
    def makeDataSource(self):
        user = 'postgres'
        password = 'postgres'
        host = 'localhost'
        dbname = 'instalike'

        dataSource = PGDataSource(user, password, host, dbname)
        return dataSource

    def test_classInstalikeDAOImplementsAllMethods(self):
        try:
            object = InstalikeDAO(self.makeDataSource())
        except TypeError:
            self.fail('Error instantiating InstalikeDAO class.')

    def test_shouldNotCreateInstalikeDAOWithoutDatasource(self):
        datasource = self.makeDataSource()
        dao = InstalikeDAO(datasource)
        self.assertIsNotNone(dao)
