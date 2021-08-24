from django import forms
from django.db import models
from django import forms
from django.http import request
from .models import Day

class DayCreateForm(forms.ModelForm):
    form = DayCreateForm(request.POST or None)

    class Meta:
        model = Day
        fields = "__all__"