from unittest import TestCase

from dbplugin.pgdatasource import PGDataSource
from dbplugin.exceptions.NotInitializedDataSourceException import NotInitializedDataSourceException


class TestPersist(TestCase):
    def makeDataSource(self):
        user = 'postgres'
        password = 'postgres'
        host = 'localhost'
        db_name = 'instalike'

        data_source = PGDataSource(user, password, host, db_name)
        return data_source

    def test_shouldCreateDataSource(self):
        dataSource = self.makeDataSource()
        dataSource.connect()
        connection = dataSource.getConnection()

        self.assertIsNotNone(connection)
        self.assertIsNotNone(dataSource)

    def test_shouldRaiseNotInitializedDataSourceException(self):
        dataSource = self.makeDataSource()

        try:
            dataSource.getConnection()
            self.fail('Calling dataSource.GetConnection() should have thrown exception NotInitializedDataSource.')
        except NotInitializedDataSourceException as e:
            pass

    def test_shouldNotConnectIfNoUserSpecified(self):
        dataSource = self.makeDataSource()
        dataSource.username = None

        response = dataSource.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfNoPasswordSpecified(self):
        dataSource = self.makeDataSource()
        dataSource.password = None

        response = dataSource.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfNoHostSpecified(self):
        dataSource = self.makeDataSource()
        dataSource.host = None

        response = dataSource.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfNoDatabaseSpecified(self):
        dataSource = self.makeDataSource()
        dataSource.database = None

        response = dataSource.connect()
        self.assertFalse(response)

    def test_dataSourceShouldConnectToDatabase(self):
        dataSource = self.makeDataSource()

        response = dataSource.connect()
        self.assertTrue(response)

    def test_shouldNotConnectIfInvalidUser(self):
        dataSource = self.makeDataSource()
        dataSource.username = 'xxxx'

        response = dataSource.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfInvalidPassword(self):
        dataSource = self.makeDataSource()
        dataSource.password = 'xxxx'

        response = dataSource.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfInvalidDatabase(self):
        dataSource = self.makeDataSource()
        dataSource.password = 'xxxx'

        response = dataSource.connect()
        self.assertFalse(response)