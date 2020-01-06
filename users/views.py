from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import (
    RegisterUserForm,
    ProfileForm,
    UserLoginForm,
    UpdateUserForm,
    UpdateProfileForm,
)
import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required
def logout(request):
    """Logout the user if he is already authenticated"""
    auth.logout(request)
    messages.success(request, f"You have successfully been logged out!")
    return redirect(reverse("home-home"))


def login(request):
    """ Return to home page if user is authenticated """
    if request.user.is_authenticated:
        return redirect(reverse("home-home"))
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=request.POST["username"], password=request.POST["password"]
            )
            if user:
                auth.login(user=user, request=request)
                messages.success(request, f"You have successfully logged in!")
                return redirect(reverse("home-home"))
            else:
                form.add_error(None, f"Your username or password is incorrect!")
    else:
        form = UserLoginForm()

    return render(request, "users/login.html", {"form": form})


def register(request):
    """Register users view.
        The user can register after paying with stripe his membership."""
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            # Stripe section
            try:
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                customer = stripe.Customer.create(
                    email=user.email, plan="plan_GNNrDYol6PdfOA", card=user.stripe_id
                )
                user.stripe_id = customer.id
                user.plan = "plan_GNNrDYol6PdfOA"
                user.save()

                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                messages.success(
                    request,
                    f"The account for {username} was created successfully! You are now able to login",
                )
                return redirect("login")
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined!")
    else:
        form = RegisterUserForm()
        profile_form = ProfileForm()
    return render(
        request,
        "users/register.html",
        {
            "form": form,
            "profile_form": profile_form,
            "publishable": settings.STRIPE_PUBLISHABLE,
        },
    )


@login_required
def profile(request):
    """User account view"""
    if request.method == "POST":
        updateForm = UpdateUserForm(request.POST, instance=request.user)
        profileUpdateForm = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if updateForm.is_valid() and profileUpdateForm.is_valid():
            updateForm.save()
            profileUpdateForm.save()
            messages.success(request, f"You have successfully updated your acount!")
            return redirect("profile")
    else:
        updateForm = UpdateUserForm(instance=request.user)
        profileUpdateForm = UpdateProfileForm(instance=request.user.profile)
    return render(
        request,
        "users/profile.html",
        {"updateForm": updateForm, "profileUpdateForm": profileUpdateForm},
    )
