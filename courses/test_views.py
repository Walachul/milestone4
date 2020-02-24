from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="Testing1", email="Testing@testing.com", password="Password1234"
        )

    def testCourse(self):
        self.client.login(username="Testing1", password="Password1234")


class TestCourses(TestCase):
    def test_courses(self):

        response = self.client.get(reverse("courses-home"))
        """ 302 Found
        From Django shell: HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/login/?next=/cart/">
        Requires login in order to view the cart
          """
        self.assertEqual(response.status_code, 302)

        self.client.login(username="Testing1", password="Password1234")
        response = self.client.get(reverse("courses-home"))
        self.assertEqual(response.status_code, 302)
