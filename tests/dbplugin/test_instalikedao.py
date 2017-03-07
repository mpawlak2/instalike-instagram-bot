from unittest import TestCase

from datalayer.dbplugin.instalikedao import InstalikeDAO

from datalayer.dbplugin.pgdatasource import PGDataSource


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
