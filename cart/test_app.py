from django.test import TestCase
from django.apps import apps
from .apps import CartConfig


class TestCartApp(TestCase):
    def test_app(self):

        self.assertEqual("cart", CartConfig.name)
        self.assertEqual("cart", apps.get_app_config("cart").name)
