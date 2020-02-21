from django.conf.urls import url

from .views import CourseList, CourseDetail

urlpatterns = [
    url(r"^$", CourseList, name="courses-home"),
    url(r"^(?P<pk>\d+)/$", CourseDetail, name="course-details"),
]

