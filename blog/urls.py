from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    url(r"^$", PostListView.as_view(), name="blog-home"),
    url(r"^(?P<pk>\d+)/$", PostDetailView.as_view(), name="blog-details-post"),
    url(r"^new/$", PostCreateView.as_view(), name="blog-new-post"),
    url(r"^(?P<pk>\d+)/update/$", PostUpdateView.as_view(), name="blog-update-post"),
    url(r"^(?P<pk>\d+)/delete/$", PostDeleteView.as_view(), name="blog-delete-post"),
    url(r"^(?P<username>\d+)/$", UserPostListView.as_view(), name="blog-user-posts"),
]

