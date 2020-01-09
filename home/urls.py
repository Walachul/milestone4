from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.home, name="home-home"),
    url(r"^partners/", views.partners, name="home-partners"),
]

