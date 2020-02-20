from django.apps import apps
from .apps import CheckoutConfig
from django.test import TestCase


class TestCheckoutConfig(TestCase):
    def test_app(self):
        self.assertEqual("checkout", CheckoutConfig.name)
        self.assertEqual("checkout", apps.get_app_config("checkout").name)

