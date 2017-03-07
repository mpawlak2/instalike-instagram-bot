from unittest import TestCase

from datalayer import PGDataSource, InstalikeSQLDAO


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
            object = InstalikeSQLDAO(self.makeDataSource())
        except TypeError:
            self.fail('Error instantiating InstalikeDAO class.')

    def test_shouldNotCreateInstalikeDAOWithoutDatasource(self):
        datasource = self.makeDataSource()
        dao = InstalikeSQLDAO(datasource)
        self.assertIsNotNone(dao)
