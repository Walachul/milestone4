from django.conf.urls import url, include
from .views import all_items

urlpatterns = [url(r"^$", all_items, name="all_items")]

