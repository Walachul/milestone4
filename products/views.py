from django.shortcuts import render
from .models import Merchandise, Clothes


def all_items(request):
    clothes = Clothes.objects.all()
    merchandise = Merchandise.objects.all()
    return render(
        request, "products/items.html", {"clothes": clothes, "merchandise": merchandise}
    )

