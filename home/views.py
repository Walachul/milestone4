from django.shortcuts import render

# Home
def home(request):
    return render(request, "home/index.html", {"title": "Home"})


# Mission/Vision/Values
def mission(request):
    return render(request, "home/mission.html", {"title": "Mission"})


# Historic


def historic(request):
    return render(request, "home/historic.html", {"title": "History"})


# Partners
def partners(request):
    return render(request, "home/partners.html", {"title": "Partners"})
