from django.db import models
from products.models import Merchandise
from django.contrib.auth.models import User

"""Get valid information from user"""


class Order(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=100, blank=False)
    county = models.CharField(max_length=100, blank=False, default="")
    city = models.CharField(max_length=100, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    street_adress1 = models.CharField(max_length=100, blank=False)
    street_adress2 = models.CharField(max_length=100, blank=False)
    date = models.DateField()
    buyer = models.ForeignKey(User, default=None)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


"""What product and how much quantity the user is buying"""


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    merchandise = models.ForeignKey(Merchandise, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.merchandise.name, self.merchandise.price
        )
