from django.shortcuts import redirect, render
from .models import Employee


def index(request):
    employees = Employee.objects.all()
    return render(request, "client_index.html", {"employees": employees})


def create_employee(request):
    if request.POST:
        name = request.POST.get("name")
        employee = Employee(name=name)
        employee.save()
        return redirect("app_index")