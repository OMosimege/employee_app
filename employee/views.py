from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee

# def home(request):
#     template = "employee/home.html"
#     context = {}

#     return render(request, template_name=template, context=context)


def employee_overview(request):
    employees = Employee.objects.all()
    if employees:
        return render(request, 'home.html', {'employees': employees})
    else:
        return render(request, 'no_employees.html')