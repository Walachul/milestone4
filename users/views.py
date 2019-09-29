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
                request, f"The account for {username} was created successfully!"
            )
            return redirect("home-home")
    else:
        form = RegisterUserForm()
    return render(request, "register.html", {"form": form})

