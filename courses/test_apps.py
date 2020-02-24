from django.apps import apps
from .apps import CoursesConfig
from django.test import TestCase


class TestCoursesConfig(TestCase):
    def test_app(self):
        self.assertEqual("courses", CoursesConfig.name)
        self.assertEqual("users", apps.get_app_config("users").name)
