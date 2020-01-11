from django.shortcuts import render

# Home page
def home(request):
    return render(request, "home/index.html", {"title": "Home"})


# Mission/Vision/Values page
def mission(request):
    return render(request, "home/mission.html", {"title": "Mission"})


# Partners page
def partners(request):
    return render(request, "home/partners.html", {"title": "Partners"})
