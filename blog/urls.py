from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.render_posts, name="blog-home"),
    url(r"^(?P<pk>\d+)/$", views.details_one_post, name="blog-details-post"),
    url(r"^new/$", views.create_edit_post, name="blog-new-post"),
    url(r"^(?P<pk>\d+)/edit/$", views.create_edit_post, name="blog-edit-post"),
]

