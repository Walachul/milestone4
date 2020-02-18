from django.test import TestCase, Client
from .views import *
from django.contrib.auth.models import User
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="Test1234"
        )

        # Test login

    def test_login(self):
        # Get login template
        template = self.client.get(reverse("login"))
        self.assertEqual(template.status_code, 200)
        self.assertTemplateUsed(template, "users/login.html")

        # Test CSRF TOken
        response = self.client.get(reverse("login"))
        self.assertContains(response, "csrfmiddlewaretoken")

        self.client.login(username="test", password="test")
        self.assertEqual(response.status_code, 200)

        # True
        self.assertFalse(self.client.login(username="test", password="wrong"))

    def test_logout(self):
        # Get logout template
        template = self.client.get(reverse("logout"), follow=True)
        self.assertEqual(template.status_code, 200)
        self.assertTemplateUsed(template, "users/logout.html")

        # Logout user
        self.client.login(username="test", password="test")
        response = self.client.get(reverse("logout"))
        """ 200 code because it renders the template,
        but requires user to log in"""
        self.assertEqual(response.status_code, 200)

        # Redirects to home template

        response = self.client.get(reverse("home-home"))
        self.assertEqual(response.status_code, 200)

    def test_user_profile(self):
        # Get profile page
        template = self.client.get(reverse("profile"))
        """
        From Django shell:
        <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/login/?next=/profile/">
        Requires the user to login to visit the profile page
        """
        self.assertEqual(template.status_code, 302)

        # Users logs in

        self.client.login(username="test", password="test")
        response = self.client.get(reverse("profile"))
        # Profile page is found
        self.assertEqual(response.status_code, 302)


class RegisterTests(TestCase):
    def setUp(self):
        url = reverse("registration")
        data = {"username": "Test1", "password": "Test1234", "password2": "Test1234"}
        self.response = self.client.post(url, data)
        self.home_url = reverse("index")
        self.profile_url = reverse("profile")

    def redirect_test(self):
        """
        Successful registration should redirect to home page
        """
        self.assertRedirects(self.response, self.home_url)

    def failed_registration(self):

        self.response = self.client.post(url, {})
        # Return same registration page
        self.assertEqual(self.response.status_code, 200)
