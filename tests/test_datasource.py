from unittest import TestCase

from datalayer import PGDataSource, NotInitializedDataSourceException


class TestPersist(TestCase):
    def makeDataSource(self):
        user = 'postgres'
        password = 'postgres'
        host = 'localhost'
        db_name = 'instalike'

        data_source = PGDataSource(user, password, host, db_name)
        return data_source

    def test_shouldCreateDataSource(self):
        data_source = self.makeDataSource()
        data_source.connect()
        connection = data_source.getConnection()

        self.assertIsNotNone(connection)
        self.assertIsNotNone(data_source)

    def test_shouldRaiseNotInitializedDataSourceException(self):
        data_source = self.makeDataSource()

        try:
            data_source.getConnection()
            self.fail('Calling data_source.GetConnection() should have thrown exception NotInitializedDataSource.')
        except NotInitializedDataSourceException as e:
            pass

    def test_shouldNotConnectIfNoUserSpecified(self):
        data_source = self.makeDataSource()
        data_source.username = None

        response = data_source.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfNoPasswordSpecified(self):
        data_source = self.makeDataSource()
        data_source.password = None

        response = data_source.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfNoHostSpecified(self):
        data_source = self.makeDataSource()
        data_source.host = None

        response = data_source.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfNoDatabaseSpecified(self):
        data_source = self.makeDataSource()
        data_source.database = None

        response = data_source.connect()
        self.assertFalse(response)

    def test_dataSourceShouldConnectToDatabase(self):
        data_source = self.makeDataSource()

        response = data_source.connect()
        self.assertTrue(response)

    def test_shouldNotConnectIfInvalidUser(self):
        data_source = self.makeDataSource()
        data_source.username = 'xxxx'

        response = data_source.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfInvalidPassword(self):
        data_source = self.makeDataSource()
        data_source.password = 'xxxx'

        response = data_source.connect()
        self.assertFalse(response)

    def test_shouldNotConnectIfInvalidDatabase(self):
        data_source = self.makeDataSource()
        data_source.password = 'xxxx'

        response = data_source.connect()
        self.assertFalse(response)