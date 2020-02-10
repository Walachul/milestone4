from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterUserForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    # Check that email is unique
    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(
                u"Email address is taken. Please choose another one."
            )
        return email

    # Save function modified in order to save first and last name of user
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
        return user


"""Extend the user table with additional information"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("homeAddress",)
        exclude = ["user"]


class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profileImage", "homeAddress"]

