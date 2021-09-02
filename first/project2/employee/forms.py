from django import forms
from django.forms.models import ModelChoiceField
from .models import Club, Department

class SearchForm(forms.Form):
    club = forms.ModelChoiceField(queryset=Club.objects, label="Club", required=False)

    department = forms.ModelChoiceField(queryset=Department.objects, label="Department", required=False)