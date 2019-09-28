from django.shortcuts import render


def home(request):
    """BLOG Home page"""

    return render(request, "home.html", {"title": "Blog"})


# Create your views here.
