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

    # Participants
    participants = models.CharField(max_length=20)
    totalParticipants = models.IntegerField(default=0)
    participant = models.ForeignKey(User, default=None)
    video_url = models.CharField(max_length=200, null=False)
    trainer = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# List of notions discussed in the course
class Notions(models.Model):

    notionDiscussed = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)


# Requirements for enrolling
class EnrollingRequirements(models.Model):

    requirementsForEnrolling = models.CharField(max_length=200, null=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)


# Gear Requirements
class GearRequirements(models.Model):

    requiredGear = models.CharField(max_length=200, null=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
