from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import stripe

Membership_Choices = (
    ("Regular Membership", "Regular"),
    ("Student Membership", "Student"),
    ("Retired Membership", "Retired"),
)

"""Membership based on 3 choices. 
   The users will have the same access to the app,
   only the price will be different based on their status."""


class Membership(models.Model):
    membership_type = models.CharField(
        choices=Membership_Choices, default="Regular membership", max_length=30
    )
    price = models.IntegerField(default=100)
    stripe_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type


"""User and the type of membership for that user"""


class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


def post_save_usermembership_create(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)
    user_membership, created = UserMembership.objects.get_or_create(user=instance)
    if (
        user_membership.stripe_customer_id is None
        or user_membership.stripe_customer_id == ""
    ):
        new_customer_id = stripe.Customer.create(email=instance.email)
        user_membership.stripe_customer_id = new_customer_id["id"]
        user_membership.save()


post_save.connect(post_save_usermembership_create, sender=User)


"""After paying, the user subscription becomes active"""


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username
