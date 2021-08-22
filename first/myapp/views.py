from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "name": "Eric",
    }

    return render(request, "myapp/index.html", context)

def about(request):
    return render(request, "myapp/index.html")

def info(request):
    return render(request, "myapp/index.html")