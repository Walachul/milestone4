from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    homeAddress = forms.CharField(max_length=200)
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)
    phoneNumber = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "firstName",
            "lastName",
            "homeAddress",
            "phoneNumber",
            "password1",
            "password2",
        ]

