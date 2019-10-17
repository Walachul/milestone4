from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterUserForm(UserCreationForm):

    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)
    birthDate = forms.DateField(help_text="Required. Format: DD-MM-YYYY")
    homeAddress = forms.CharField(max_length=200)
    phoneNumber = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "firstName",
            "lastName",
            "birthDate",
            "homeAddress",
            "phoneNumber",
            "password1",
            "password2",
        ]


class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateUserForm(forms.ModelForm):
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
        ]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profileImage"]

