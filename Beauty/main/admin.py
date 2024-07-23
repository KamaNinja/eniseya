from django.contrib import admin

from .models import ServiceCategory, Service, Employee, Gallery
from .utils import ShortDetailsAdminMixin


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(ShortDetailsAdminMixin):
    pass


@admin.register(Gallery)
class GalleryAdmin(ShortDetailsAdminMixin):
    pass