from django.urls import path, include
from employee import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('employees/', views.employee_overview, name='employee_overview'),

    # path('create_order/', views.create_update_employee, name='create_employee'),
]