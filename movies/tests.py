from django.test import TestCase
from movies.models import Watchlist
from django.urls import reverse


class AuthTests(TestCase):

    def test_not_auth(self):
        """
        Test checks if user is not loged in
        and redirects to login page.
        """
        response = self.client.get(reverse('movies:watchlist'))
        self.assertRedirects(response, '/login/?next=/watchlist', status_code = 302)
