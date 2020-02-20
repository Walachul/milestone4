from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .views import view_cart


class TestCartView(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(
            username="Test", email="test@test.com", password="password1234"
        )

    def test_cart_view(self):

        response = self.c.get(reverse("view_cart"))
        """ 302 Found
        From Django shell: HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/login/?next=/cart/">
        Requires login in order to view the cart
          """
        self.assertEqual(response.status_code, 302)

        # 200 response

        self.c.login(username="Test", password="password1234")
        response = self.c.get(reverse("view_cart"))
        self.assertEqual(response.status_code, 200)
