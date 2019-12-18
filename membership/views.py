from django.shortcuts import render

from django.views.generic import ListView
from .models import Membership

# Select membership out of 3 available
class MembershipSelect(ListView):
    model = Membership

    template_name = "users/register.html"

    context_object_name = "memberships"
