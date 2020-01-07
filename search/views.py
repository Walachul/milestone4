from django.shortcuts import render
from products.models import Merchandise

# Create your views here.


def search_merch(request):
    merchandise = Merchandise.objects.filter(name__icontains=request.GET["q"])
    return render(request, "products/items.html", {"merchandise": merchandise})
