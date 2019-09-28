from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def render_posts(request):
    """Render all posts in the home page template of the Blog app"""

    posts = Post.objects.filter(dateAdded).order_by("-dateAdded")
    return render(request, "home.html", {"title": "Blog Home"}, {"posts": posts})


def details_one_post(request, pk):

    """Render a single post with more details
     about it based  on ID or return 404 if not found"""

    post = get_object_or_404(Post, pk=pk)
    post.save()
    return render(request, "post_details", {"title": post.title}, {"post": post})


def create_edit_post(request, pk=none):

    """Create a post or edit one based on ID"""

    return render(request, "home.html", {"title": "Blog Home"}, {"posts": posts})
