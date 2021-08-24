from .forms import DayCreateForm
from django.shortcuts import render, redirect
from .models import Day

# Create your views here.
def index(request):
    return render(request, "diary/day_list.html")

def add(request):
    form = DayCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid:
        form.save()
        return redirect("diary:index")

    context = {
        'form': DayCreateForm()
    }
    return render(request, "diary/day_form.html", context)