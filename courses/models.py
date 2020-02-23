from django.db import models
from django.utils import timezone
from products.models import Product


class Courses(Product):

    description = models.TextField()
    dateAdded = models.DateTimeField(default=timezone.now)
    # Time period in which the course is organized
    periodOfTime = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    # Participants
    participants = models.CharField(max_length=20)
    totalParticipants = models.IntegerField(default=0)
    """In order to get the correct video_url and render it in the iframe,
        you have to get the Embed Video from YouTube and get link as:
        https://www.youtube.com/embed/exampleVideo
        and paste it in the admin panel
     """
    video_url = models.CharField(max_length=200, null=True, blank=True)
    trainer = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# List of notions discussed in the course
class Notions(models.Model):

    notionDiscussed = models.CharField(max_length=100, null=True, blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.notionDiscussed


# Requirements for enrolling
class EnrollingRequirements(models.Model):

    requirementsForEnrolling = models.CharField(max_length=200, null=True, blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.requirementsForEnrolling


# Gear Requirements
class GearRequirements(models.Model):

    requiredGear = models.CharField(max_length=200, null=True, blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.requiredGear
