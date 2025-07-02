from .views import index, create_employee
from django.urls import path

urlpatterns = [
    path('', index, name='app_index'),
    path('create_employee', create_employee, name='create_employee')
]
