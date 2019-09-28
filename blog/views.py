from django.shortcuts import render
from .models import Post


def home(request):
    """BLOG Home page"""
    posts = Post.objects.all()
    return render(request, "home.html", {"title": "Blog"}, {"posts": posts})


# Create your views here.
