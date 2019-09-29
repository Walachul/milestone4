from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import BlogForm


def render_posts(request):
    """Render all posts in the home page template of the Blog app"""

    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


def details_one_post(request, pk):

    """Render a single post with more details
     about it based  on ID or return 404 if not found"""

    post = get_object_or_404(Post, pk=pk)
    post.save()
    return render(request, "post_details.html", {"post": post})


def create_edit_post(request, pk=None):

    """Create a post or edit one based on ID status if null or not."""

    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(details_one_post, post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, "blog_form.html", {"form": form})
