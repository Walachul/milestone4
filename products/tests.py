from django.test import TestCase
from .models import Merchandise, Clothes


class TestMerch(TestCase):
    def test_str(self):
        test_name = Merchandise(name="A product")
        self.assertEqual(str(test_name), "A product")


class TestClothes(TestCase):
    def test_str(self):
        test_name = Clothes(name="Rainproof jacket")
        self.assertEqual(str(test_name), "Rainproof jacket")

