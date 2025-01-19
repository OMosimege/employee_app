from django.urls import path
from .views import employee_list, new_employee

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('new/', new_employee, name='new_employee'),
]