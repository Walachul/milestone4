from django.apps import apps
from .apps import ProductsConfig
from django.test import TestCase


class TestProductsConfig(TestCase):
    def test_app(self):
        self.assertEqual("products", ProductsConfig.name)
        self.assertEqual("users", apps.get_app_config("users").name)
