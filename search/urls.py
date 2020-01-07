from django.conf.urls import url
from .views import search_merch

urlpatterns = [url(r"^$", search_merch, name="search")]

