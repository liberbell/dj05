from .forms import DayCreateForm
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "diary/day_list.html")

def add(request):
    context = {
        'form': DayCreateForm()
    }
    return render(request, "diary/day_form.html", context)