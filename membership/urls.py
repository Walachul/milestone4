from django.conf.urls import url
from .views import MembershipSelect

urlpatters = [url(r"^$", MembershipSelect.as_view(), name="Membership-select")]

