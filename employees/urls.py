from django.urls import path
from .views import employee_list, new_employee, edit_employee

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('new/', new_employee, name='new_employee'),
    path('<str:employee_id>/edit/', edit_employee, name='edit_employee'),
]

