import re
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "diary/day_list.html")

def add(request):
    return