from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register users"""

    form = UserCreationForm()
    return render(request, "register.html", {"form": form})

