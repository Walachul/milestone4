from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "firstName",
            "lastName",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.firstName = self.cleaned_data["firstName"]
        user.lastName = self.cleaned_data["lastName"]

        if commit:
            user.save()
        return user


"""Extend the user table with additional information"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("birthDate", "homeAddress", "phoneNumber")


class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "firstName", "lastName"]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profileImage", "homeAddress", "phoneNumber"]

