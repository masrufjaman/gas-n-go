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


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.age = 20
        self.password = 'password'

    def test_signup_page_url(self):
        response = self.client.get("/users/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_form(self):
        response = self.client.post(reverse('register'), data={
            'username': self.username,
            'email': self.email,
            'age': self.age,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
