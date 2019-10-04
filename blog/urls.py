from django.conf.urls import url
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    url(r"^$", PostListView.as_view(), name="blog-home"),
    url(r"^(?P<pk>\d+)/$", PostDetailView.as_view(), name="blog-details-post"),
    url(r"^new/$", views.create_edit_post, name="blog-new-post"),
    url(r"^(?P<pk>\d+)/edit/$", views.create_edit_post, name="blog-edit-post"),
]

