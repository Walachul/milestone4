from django.shortcuts import render
from products.models import Merchandise
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def search_merch(request):
    merchandise = Merchandise.objects.filter(name__icontains=request.GET["q"])
    return render(request, "products/items.html", {"merchandise": merchandise})
