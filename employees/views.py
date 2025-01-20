from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import render
from django.shortcuts import redirect


def employee_list(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        else:
            return render(request, 'employees/employee_list.html', {
                'employees': employees,
                'form': form,
                'show_modal': True
            })

    form = EmployeeForm()
    return render(request, 'employees/employee_list.html', {
        'employees': employees,
        'form': form,
        'show_modal': False
    })


def new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employees/new_employee.html', {'form': form})

