from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from .models import Customer
from django.test import TestCase


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        Customer.objects.create_user(**self.credentials)

    def test_login(self):
        # login
        response = self.client.post('/login/', **self.credentials)
        # should be logged in now, fails however
        self.assertTrue(response.context['user'].is_active)
