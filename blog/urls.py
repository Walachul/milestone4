from django.conf.urls import url
from . import views

urlpatterns = [url(r"^$", views.render_posts, name="blog-home")]

