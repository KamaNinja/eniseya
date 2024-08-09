from django.shortcuts import render

from .models import Service, Employee, Gallery
from .forms import FilterGalleryForm


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'main/index.html', context)


def get_services(request):
    services = Service.active_objects.all().select_related('service_category')
    context = {'title': 'Услуги', 'services': services}
    return render(request, 'main/services.html', context)


def get_employees(request):
    employees = Employee.active_objects.all().prefetch_related('gallery_set')
    context = {'title': 'Мастера', 'employees': employees}
    return render(request, 'main/employees.html', context)


def get_gallery(request):
    filter_form = FilterGalleryForm(request.GET)

    selected_categories = request.GET.getlist('service_category')
    selected_employees = request.GET.getlist('employee')

    gallery = filter_form.filter_gallery(Gallery, selected_categories, selected_employees)

    context = {
        'title': 'Галерея',
        'gallery': gallery,
        'form': filter_form,
    }

    return render(request, 'main/gallery.html', context)
