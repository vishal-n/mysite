from django.shortcuts import render

# Create your views here.
def geeks_view(request):

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home_page.html")
