from unittest import TestCase

from datasource import DataSource


class TestPersist(TestCase):
    def makeDataSource(self):
        user = 'postgres'
        password = 'postgres'
        host = 'localhost'
        dbname = 'instamanager'

        dataSource = DataSource(user, password, host, dbname)
        return dataSource

    def test_shouldCreateDataSource(self):
        dataSource = self.makeDataSource()

        self.assertIsNotNone(dataSource)

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
