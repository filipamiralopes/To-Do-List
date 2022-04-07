"""File containing helpers for testing."""

from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITransactionTestCase


class NewUserTestCase(APITransactionTestCase):  # to prevent test data to stay in the db across multiple tests
    """
    Sets up, creates and removes users in the test database.
    """
    def setUp(self) -> None:
        super().setUp()
        self.username = "sauron"
        self.email = "sauron@mordor.one"
        self.password = "sauron"
        self.user = User.objects.create_user(username=self.username,
                                             email=self.email,
                                             password=self.password)
        self.client = APIClient()
        self.client.login(username=self.username, password=self.password)

    def tearDown(self) -> None:
        super().tearDown()
