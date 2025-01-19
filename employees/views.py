from .models import Employee
from django.shortcuts import render


def employee_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees/employee_list.html', context)