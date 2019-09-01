from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """BLOG HOme page"""

    return HttpResponse("<h1>Blog Home</h1>")


def about(request):
    """BLOG HOme page"""

    return HttpResponse("<h1>Blog About</h1>")


# Create your views here.
