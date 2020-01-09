from django.shortcuts import render

# Home page
def home(request):
    return render(request, "home/index.html", {"title": "Home"})


# Partners page
def partners(request):
    return render(request, "home/partners.html", {"title": "Partners"})
