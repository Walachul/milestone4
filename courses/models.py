from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Courses(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    dateAdded = models.DateTimeField(default=timezone.now)
    # Time period in which the course is organized
    periodOfTime = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    scopeOfCourse = models.CharField(max_length=200)
    # Notions that will be discussed/learned during the course
    notionDiscussed = models.TextField()
    # Requirements for enrolling
    requirementsForEnrolling = models.CharField(max_length=200, null=False)
    requiredGear = models.CharField(max_length=200)
    # Participants
    participants = models.CharField(max_length=20)
    participant = models.ForeignKey(User, default=None)
    trainer = models.CharField(max_length=100)
