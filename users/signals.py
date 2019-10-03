from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


"""When a user is saved(created) send post_save signal. Signal is received by @receiver.
    After this, with the arguments from the create_profile function, the user profile
    is created based on the instance of the user that was created. """


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)


"""Save the profile whenever User is saved"""


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
