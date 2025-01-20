from .models import Employee, Skill
from .forms import EmployeeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse


def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()

    # Get distinct years of birth and available skills
    years = Employee.objects.dates('date_of_birth', 'year').distinct()
    skills = Skill.objects.all()

    # Search employees
    search_query = request.GET.get('search')
    if search_query:
        employees = employees.filter(
            first_name__icontains=search_query
        ) | employees.filter(
            last_name__icontains=search_query
        ) | employees.filter(
            email__icontains=search_query
        )

    # Filter employees
    filter_query = request.GET.get('filter')
    if filter_query:
        if filter_query.startswith('year_'):
            year = filter_query.split('_')[1]
            employees = employees.filter(date_of_birth__year=year)
        elif filter_query.startswith('skill_'):
            skill_id = filter_query.split('_')[1]
            employees = employees.filter(skills__id=skill_id)

    # Handle form submission for adding employees
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        else:
            return render(request, 'employees/employee_list.html', {
                'employees': employees,
                'form': form,
                'show_modal': True,
                'years': years,
                'skills': skills,
            })

    form = EmployeeForm()
    return render(request, 'employees/employee_list.html', {
        'employees': employees,
        'form': form,
        'show_modal': False,
        'years': years,
        'skills': skills,
    })


def new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = EmployeeForm()
    return render(request, 'employees/new_employee.html', {'form': form})

def delete_employee(request, employee_id):
    """Delete an employee record."""
    if request.method == 'POST':
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            employee.delete()
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Employee not found.'})
    return JsonResponse({'success': False, 'error': 'Invalid request.'})
