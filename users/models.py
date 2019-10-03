from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extending the user profile by adding image field.
        On delete argument CASCADE > when the user is deleted, his profile is deleted also,
        but if profile is deleted, user is not."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(default="default.jpg", upload_to="profile_images")

    def __str__(self):
        return f"{self.user.username} Profile"
