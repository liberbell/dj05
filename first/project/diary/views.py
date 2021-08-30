from .forms import DayCreateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Day

class indexView(generic.ListView):
    model = Day
    paginate_by = 3

class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

# class UpdateView(generic.UpdateView):
#     model = Day
#     form_class = DayCreateForm
#     success_url = reverse_lazy('diary:index')

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')

class DetailView(generic.DetailView):
    model = Day

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

def update(request, pk):
    day = get_object_or_404(Day, pk=pk)

    form = DayCreateForm(request.POST or None, instance=day)

    if request.method == "POST" and form.is_valid:
        form.save()
        return redirect("diary:index")

    context = {
        "form": form
    }
    return render(request, "diary/day_form.html", context)

def delete(request, pk):
    day = get_object_or_404(Day, pk=pk)

    if request.method == "POST":
        day.delete()
        return redirect("diary:index")

    context = {
        "day": day,
    }
    return render(request, "diary/day_confirm_delete.html", context)

def detail(request, pk):
    day = get_object_or_404(Day, pk=pk)

    if request.method == "POST":
        day.delete()
        return redirect("diary:index")

    context = {
        "day": day,
    }
    return render(request, "diary/day_detail.html", context)