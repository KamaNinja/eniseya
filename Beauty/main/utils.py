from django.db import models
from django.contrib import admin
from django.utils.text import slugify

import datetime
from pathlib import Path

from unidecode import unidecode


def get_unique_slug(model, field):
    slug = slugify(unidecode(field))
    unique_slug = slug
    count = 1

    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{count}"
        count += 1

    return unique_slug


class UniqueNameImageModelMixin(models.Model):
    def generate_unique_name(self):
        now = datetime.datetime.now()
        class_name = self.__class__.__name__.lower()
        unique_name = f"{class_name}_{now.strftime('%Y%m%d_%H%M%S')}"
        return unique_name

    def get_upload_path(self, filename):
        ext = Path(filename).suffix
        filename = f"{self.generate_unique_name()}{ext}"
        return f"{self.__class__.__name__}/{filename}"

    photo = models.ImageField(upload_to=get_upload_path)

    class Meta:
        abstract = True


class ShortDetailsAdminMixin(admin.ModelAdmin):
    def short_details(self, obj):
        details = obj.details or '-'
        return details[:25] + '...' if len(details) > 25 else details

    short_details.short_description = 'Детали'
    short_details.admin_order_field = 'details'
