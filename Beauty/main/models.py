from django.core.validators import MinValueValidator
from django.db import models

from .utils import UniqueNameImageModelMixin


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ServiceCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                blank=True,
                                null=True,
                                validators=[MinValueValidator(0.1)])
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.PROTECT)


class Employee(UniqueNameImageModelMixin, models.Model):
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    object = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return self.name


class Gallery(UniqueNameImageModelMixin, models.Model):
    details = models.CharField(max_length=255)
    stylist = models.ForeignKey('Employee', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.PROTECT)
    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        pass