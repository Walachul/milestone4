from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterUserForm, UserLoginForm


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

    return render(request, "login.html", {"form": form})


def register(request):
    """Register users view"""
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"The account for {username} was created successfully! You are now able to login",
            )
            return redirect("login")
    else:
        form = RegisterUserForm()
    return render(request, "register.html", {"form": form})


def account(request):
    """User account view"""

    return render(request, "account.html")
