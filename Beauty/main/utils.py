from django.db import models
from django.contrib import admin

import datetime
from pathlib import Path


class UniqueNameImageModelMixin(models.Model):
    """
    Этот миксин предназначен для использования в качестве базового класса для моделей,
    которые хранят изображения или другие файлы. Он обеспечивает генерацию уникального
    имени файла и определение пути для загрузки файла, что помогает избежать конфликтов
    имен и организовать файлы в соответствии с именем класса.
    """
    def generate_unique_name(self):
        now = datetime.datetime.now()
        class_name = self.__class__.__name__.lower()
        unique_name = f"{class_name}_{now.strftime('%Y%m%d_%H%M%S')}"
        return unique_name

    def get_upload_path(self, filename):
        ext = Path(filename).suffix
        filename = f"{self.generate_unique_name()}{ext}"
        return f"{self.__class__.__name__}/{filename}"

    class Meta:
        abstract = True


class ShortDetailsAdminMixin(admin.ModelAdmin):
    """
    Миксин для Django Admin, который добавляет новое поле "Детали" в список элементов.
    Это поле будет содержать краткую версию поля `details` объекта, обрезая его до 25 символов.
    """
    def short_details(self, obj):
        details = obj.details or '-'
        return details[:25] + '...' if len(details) > 25 else details

    short_details.short_description = 'Детали'
    short_details.admin_order_field = 'details'
