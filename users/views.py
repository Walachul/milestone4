from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    """Register users view"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"The account for {username} was created successfully!"
            )
            return redirect("home-home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

