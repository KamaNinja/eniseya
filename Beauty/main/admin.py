from django.contrib import admin

from .models import ServiceCategory, Service, Employee, Gallery
from .utils import ShortDetailsAdminMixin


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    exclude = ('slug',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('title',)


@admin.register(Employee)
class EmployeeAdmin(ShortDetailsAdminMixin):
    list_display = ('name', 'slug')
    exclude = ('slug',)


@admin.register(Gallery)
class GalleryAdmin(ShortDetailsAdminMixin):
    pass