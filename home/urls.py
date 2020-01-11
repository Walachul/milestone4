from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.home, name="home-home"),
    url(r"^historic/", views.historic, name="home-historic"),
    url(r"^mission/", views.mission, name="home-mission"),
    url(r"^partners/", views.partners, name="home-partners"),
]

