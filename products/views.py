from django.shortcuts import render
from .models import Merchandise


def all_items(request):

    merchandise = Merchandise.objects.all()
    return render(request, "products/items.html", {"merchandise": merchandise})

