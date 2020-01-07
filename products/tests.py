from django.test import TestCase
from .models import Merchandise


class TestMerch(TestCase):
    def test_str(self):
        test_name = Merchandise(name="A product")
        self.assertEqual(str(test_name), "A product")

