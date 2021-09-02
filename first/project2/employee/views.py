from django.http import request
from django.views import generic
from .models import Employee
from .forms import SearchForm

# Create your views here.
class IndexView(generic.ListView):
    model = Employee

    def get_context_data(self):
        context = super().get_context_data()
        context["form"] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        form = SearchForm(self.request.Get)
        form.is_valid()

        queryset = super().get_queryset
        department = form.cleaned_data()
        if department:
            queryset = queryset.filter(department=department)

        club = form.cleaned_data()
        if club:
            queryset = queryset.filter(club=club)
        return queryset