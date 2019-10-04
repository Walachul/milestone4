from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import BlogForm


def render_posts(request):
    """Render all posts in the home page template of the Blog app"""

    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


class PostListView(ListView):

    """Render all posts as list using class-based view offered by django"""

    model = Post
    """Changed the template name.
     Convention for Django is to use <app>/<model>_<viewtype>.html"""

    template_name = "blog/home.html"
    """Renamed variable objectList which ListView expects when passing it to the template."""

    context_object_name = "posts"

    ordering = ["-dateAdded"]


class PostDetailView(DetailView):

    """Render all posts as list using class-based view offered by django"""

    model = Post
    """To render this template, 
    I am going to stick to the Django convention: 
    <app>/<model>_<viewtype>.html"""


def create_edit_post(request, pk=None):

    """Create a post or edit one based on ID status if null or not."""

    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(details_one_post, post.pk)
    else:
        form = BlogForm(instance=post)
    return render(request, "blog_form.html", {"form": form})
