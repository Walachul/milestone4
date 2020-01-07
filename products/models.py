from django.db import models

"""
General items like cups, hats, water recipients etc.,
with the Romanian Alpine Club Logo
"""


class Merchandise(models.Model):

    name = models.CharField(max_length=300, default="")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name


"""
Personalized clothes with the Romanian Alpine Logo
"""


class Clothes(models.Model):
    CLOTHES_SIZE = (("Small", "S"), ("Large", "L"), ("Extra large", "XL"))
    name = models.CharField(max_length=300, default="")
    description = models.TextField()
    size = models.CharField(choices=CLOTHES_SIZE, default="", max_length=30)
    specs = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

