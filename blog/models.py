from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    dateAdded = models.DateTimeField(default=timezone.now)
    # If User(author) of post gets deleted, his post(s) is deleted as well.
    authorPost = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
