from django.db import models
from django.contrib.auth.models import User


Membership_Choices = ["Regular membership", "Student membership", "Retired membership"]

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


class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
