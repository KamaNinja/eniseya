from django.shortcuts import render

from .models import Service, Employee, Gallery


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'main/index.html', context)


def get_employees(request):
    employees = Employee.active_objects.all()
    context = {'title': 'Мастера', 'employeess': employees}
    return render(request, 'main/employees.html', context)


def get_services(request):
    services = Service.active_objects.all()
    context = {'title': 'Услуги', 'services': services}
    return render(request, 'main/services.html', context)


def get_gallery(request):
    gallery = Gallery.active_objects.all()
    context = {'title': 'Галерея', 'gallery': gallery}
    return render(request, 'main/gallery.html', context)