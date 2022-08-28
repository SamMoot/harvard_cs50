from django.shortcuts import render
import datetime 
from django.http import HttpResponse
# Create your views here.


def index(request):
    now = datetime.datetime.now()
    return render(request, "anniversary/index.html", {
        "anniversary": now.month ==12 and now.day ==17
    }
    )

# def index(request):
#     return HttpResponse("profile-samantha")



# def index(request):
#     return render(request, "hello/index.html")

# def greet(request, name):
#     return render(request, "hello/greet.html", {
#         "name":name.capitalize()
#     })