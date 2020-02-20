from django.test import TestCase
from .forms import UserLoginForm, RegisterUserForm


class TestUserLoginForm(TestCase):
    # is valid data
    def test_UserLoginForm_isvalid(self):

        form = UserLoginForm(data={"username": "Test", "password": "pass"})
        self.assertTrue(form.is_valid())

    # missing field
    def test_missing_req_field(self):
        form = UserLoginForm({"username": "Test"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password"], [u"This field is required."])


class TestUserRegistrationForm(TestCase):
    # is valid data
    def test_RegisterUserForm(self):
        form = RegisterUserForm(
            data={
                "username": "Test",
                "email": "test@test.com",
                "first_name": "TestOne",
                "last_name": "TestTwo",
                "password1": "pass1234",
                "password2": "pass1234",
            }
        )
        self.assertTrue(form.is_valid())

    # Password mismatch

    def test_password_mismatch(self):
        form = RegisterUserForm(
            data={
                "username": "Test",
                "email": "test@test.com",
                "first_name": "TestOne",
                "last_name": "TestTwo",
                "password1": "pass1234",
                "password2": "pass",
            }
        )
        self.assertEqual(
            form.errors["password2"], [u"The two password fields didn't match."]
        )

