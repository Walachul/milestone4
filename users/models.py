from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    """Extending the user profile by adding additional information.
        On delete argument CASCADE > when the user is deleted, his profile is deleted also,
        but if profile is deleted, user is not."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional information required for registration
    firstName = models.CharField(max_length=50, default="First Name")
    lastName = models.CharField(max_length=50, default="Last Name")
    birthDate = models.DateField(blank=True, null=True)
    homeAddress = models.CharField(max_length=200, default="Your home address")
    phoneNumber = models.CharField(max_length=20, default="0766 xxx xxx")
    profileImage = models.ImageField(default="default.jpg", upload_to="profile_images")

    def __str__(self):
        return f"{self.user.username} Profile"

    """
    Profile is created using a Signal.
    """

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def update_profile(sender, instance, created, **kwargs):
        if created:
            instance.profile.save()

    """Override save function in order to resize the image,
        so that the file system will not get loaded with big files,
        affecting performance."""

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     imgProfile = Image.open(self.profileImage.path)

    #     if imgProfile.height > 300 or imgProfile.width > 300:
    #         outputSize = (300, 300)
    #         imgProfile.thumbnail(outputSize)
    #         imgProfile.save(self.profileImage.path)

