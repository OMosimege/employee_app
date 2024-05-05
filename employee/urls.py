from django.urls import path, include
from employee import views

urlpatterns = [
    path("", views.home, name="home"),
]