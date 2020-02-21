from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Courses


class Courses(LoginRequiredMixin, ListView):

    model = Courses

    template_name = "courses/courses.html"

    context_object_name = "courses"

