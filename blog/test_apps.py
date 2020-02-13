from django.apps import apps
from .apps import BlogConfig
from django.test import TestCase


class TestBlogConfig(TestCase):
    def test_app(self):
        self.assertEqual("blog", BlogConfig.name)
        self.assertEqual("users", apps.get_app_config("users").name)
