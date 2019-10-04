from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


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


class PostCreateView(LoginRequiredMixin, CreateView):
    """Create new post"""

    model = Post
    fields = ["title", "content", "category"]
    """Method to validate author of the post, before the form is posted.
        Otherwise, Django raises Integrity Error"""

    def form_valid(self, form):
        """Author of the instance is set as the current logged in user, 
        before submitting the form."""
        form.instance.authorPost = self.request.user
        """validate now the form, after the author is set to current auth user."""
        return super().form_valid(form)

