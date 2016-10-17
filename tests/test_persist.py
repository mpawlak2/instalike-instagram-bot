from unittest import TestCase

from datasource import DataSource
from persistlayer import PersistLayer
from repository import Repository


class TestPersist(TestCase):
    def test_shouldNotInstantiateAbstractClass(self):
        self.assertRaises(NotImplementedError, PersistLayer)

    def test_shouldInstantiateConcreteClass(self):
        testRepo = Repository()

        self.assertIsNotNone(testRepo, 'Test repo is None')
        self.assertIsInstance(testRepo, Repository)

    def makeDataSource(self):
        user = 'user'
        password = 'password'
        host = 'host'
        dbname = 'dbname'

        dataSource = DataSource(user, password, host, dbname)
        return dataSource

    def test_shouldCreateDataSource(self):
        dataSource = self.makeDataSource()

        self.assertIsNotNone(dataSource)

    def test_dataSourceShouldConnectToDatabase(self):
        dataSource = self.makeDataSource()


