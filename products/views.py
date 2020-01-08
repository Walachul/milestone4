from django.shortcuts import render
from .models import Merchandise
from django.contrib.auth.decorators import login_required


@login_required()
def all_items(request):

    merchandise = Merchandise.objects.all()
    return render(request, "products/items.html", {"merchandise": merchandise})

