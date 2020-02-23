from django.db import models
from django.utils import timezone


""" Concrete base class Model for both Merchandise and Courses models
    https://realpython.com/modeling-polymorphism-django-python/
    in order to store the common fields: ID, TITLE, PRICE,
    so as to access the Product Model in the cart session which
    will store two different items(Courses and Merchandise) based on ID
    and also to use the same model for the checkout app.
"""


class Product(models.Model):
    title = models.CharField(max_length=200, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2, default="0")

    def __str__(self):
        return self.title


"""
General items like cups, hats, water recipients etc.,
with the Romanian Alpine Club Logo
"""


class Merchandise(Product):

    description = models.TextField()
    image = models.ImageField(upload_to="images")

