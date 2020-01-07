from django.conf.urls import url
from .views import view_cart, add_to_cart, modify_cart

urlpatterns = [
    url(r"^$", view_cart, name="view-cart"),
    url(r"^add/(?P<id>\d+)", add_to_cart, name="add-to-cart"),
    url(r"^modify/(?P<id>\d+)", modify_cart, name="modify-cart"),
]

