from .forms import DayCreateForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Day

# Create your views here.
def index(request):
    context = {
        "day_list": Day.objects.all(),
    }
    return render(request, "diary/day_list.html", context)

def add(request):
    form = DayCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid:
        form.save()
        return redirect("diary:index")

    context = {
        'form': DayCreateForm()
    }
    return render(request, "diary/day_form.html", context)