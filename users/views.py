from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUserForm


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

def login(request):
    """ Return login page """
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
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse("home"))
            else:
                form.add_error(None, "Your username or password is incorrect!")
    else:
        form = UserLoginForm()

    return render(request, "login.html", {"form": form})