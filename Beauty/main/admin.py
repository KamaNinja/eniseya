from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ServiceCategory, Service, Employee, Gallery


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
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    exclude = ['slug']
    # inlines = [SimpleInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'duration',
        'price',
        'is_active',
        'service_category',
        'created_at',
        'updated_at'
    ]
    list_display_links = ['id', 'title']
    list_select_related = ['service_category']
    list_filter = ['service_category__title', 'created_at', 'updated_at']
    search_fields = ['title']
    ordering = ['service_category', 'id']
    readonly_fields = ['created_at', 'updated_at']

    actions = [activate_status, deactive_status]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'details', 'get_photo', 'is_active']
    list_display_links = ['id', 'name', 'details']
    exclude = ['slug']
    actions = [activate_status, deactive_status]
    fields = ['name', 'details', 'photo', 'is_active']

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")

    get_photo.short_description = 'Фото'


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'details',
        'stylist',
        'service_category',
        'photo',
        'is_active',
        'created_at',
        'updated_at'
    ]
    list_display_links = ['id', 'details']
    list_select_related = ['service_category']
    list_filter = ['service_category__title', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    actions = [activate_status, deactive_status]
