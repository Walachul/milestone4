from django.apps import apps
from .apps import HomeConfig
from django.test import TestCase


class TestHomeConfig(TestCase):
    def test_app(self):
        self.assertEqual("home", HomeConfig.name)
        self.assertEqual("users", apps.get_app_config("users").name)
