from django.shortcuts import render
from products.models import Merchandise

# Create your views here.


def search_merch(request):
    merchs = Merchandise.objects.filter(name__icontains=request.GET["q"])
    return render(request, "items.html", {"items": items})
