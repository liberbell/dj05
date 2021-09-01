from first.project2.employee.models import Employee
from django import template
from django.shortcuts import render
from django.views import generic
from .models import Employee

# Create your views here.
class IndexView(generic.ListView):
    model = Employee