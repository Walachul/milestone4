from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import StripePayForm, OrderForm
from .views import checkout
from django.urls import reverse
from django.utils import timezone


class TestCheckoutView(TestCase):
    def setUp(self):

        self.c = Client()
        self.user = User.objects.create_user(
            username="Test", email="test@test.com", password="Password1234"
        )
        url = reverse("checkout")
        self.response = self.c.get(url)

    def test_checkout_page(self):

        """
        302 found
        Django shell: <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/login/?next=/checkout/">
        Requires login
        """

        response = self.c.get(reverse("checkout"))
        self.assertEqual(response.status_code, 302)

        # Access page with dummy login and get 200
        self.c.login(username="Test", password="Password1234")
        response = self.c.get(reverse("checkout"))
        self.assertEqual(response.status_code, 200)

    def forms_exist(self):
        self.c.login(username="Test", password="Password1234")
        response = self.c.get(reverse("checkout"))
        formOrder = response.context.get("order_form")
        formPayment = response.context.get("stripe_form")
        self.assertIsInstance(formOrder, OrderForm)
        self.assertIsInstance(formPayment, StripePayForm)

    def test_order(self):
        self.c.login(username="Test", password="Password1234")
        data = {
            "full_name": "Name LastName",
            "phone_number": "personal_number",
            "country": "Romania",
            "postcode": "334521",
            "town_or_city": "Bucharest",
            "street_address1": "Street Test 1",
            "street_address2": "StreetTest2",
            "county": "Bucharest",
        }
        data["date"] = timezone.now()
        data["buyer"] = self.user.id
        response = self.c.post(reverse("checkout"), data)
        self.assertEqual(response.status_code, 200)
