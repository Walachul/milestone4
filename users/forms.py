from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    # Fields for Stripe
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label="Credit card number")
    cvv = forms.CharField(label="Security code (CVV)")
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "stripe_id",
        ]
        exclude = ["username"]

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
        fields = ("birthDate", "homeAddress", "phoneNumber")
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
        fields = ["profileImage", "homeAddress", "phoneNumber"]

