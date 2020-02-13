from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="Testing1", email="Testing@testing.com", password="1234"
        )

    def testPost(self):
        self.client.login(username="Testing1", password="1234")


class TestPosts(TestCase):
    def test_posts(self):

        response = self.client.get(reverse("posts:index"))
        self.assertEqual(response.status_code, 200)

