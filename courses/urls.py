from django.conf.urls import url

from .views import Courses

urlpatterns = [url(r"^$", Courses.as_view(), name="courses-home")]

