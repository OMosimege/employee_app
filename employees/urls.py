from django.urls import path
from .views import employee_list, new_employee, edit_employee, delete_employee

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('new/', new_employee, name='new_employee'),
    path('<str:employee_id>/edit/', edit_employee, name='edit_employee'),
    path('<str:employee_id>/delete/', delete_employee, name='delete_employee')
]

