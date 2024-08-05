from django.contrib import admin

from .models import ServiceCategory, Service, Employee, Gallery

import admin_thumbnails


# class SimpleInline(admin.TabularInline):
#     model = Service
#     extra = 1
#     can_delete = False


@admin.action(description='Активировать записи')
def activate_status(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Деактивировать записи')
def deactive_status(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    exclude = ['slug']
    # inlines = [SimpleInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'duration', 'price', 'is_active', 'service_category']
    list_select_related = ['service_category']
    search_fields = ['title']
    actions = [activate_status, deactive_status]


@admin.register(Employee)
@admin_thumbnails.thumbnail('photo')
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'details', 'is_active', 'photo_thumbnail']
    exclude = ['slug']
    actions = [activate_status, deactive_status]


@admin.register(Gallery)
@admin_thumbnails.thumbnail('photo')
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'details', 'stylist', 'is_active', 'service_category', 'photo_thumbnail']
    list_select_related = ['service_category']
    actions = [activate_status, deactive_status]



