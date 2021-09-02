from first.project2.employee.forms import SearchForm
from django.views import generic
from .models import Employee

# Create your views here.
class IndexView(generic.ListView):
    model = Employee

    def get_context_data(self):
        context = super().get_context_data()
        context["form"] = SearchForm(self.request.GET)
        return context