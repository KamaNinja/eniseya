from django.core.validators import MinValueValidator
from django.db import models

from .utils import UniqueNameImageModelMixin


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ServiceCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                blank=True,
                                null=True,
                                validators=[MinValueValidator(0.1)])
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.PROTECT)
    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['service_category', 'title']


class Employee(UniqueNameImageModelMixin, models.Model):
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return self.name


class Gallery(UniqueNameImageModelMixin, models.Model):
    details = models.CharField(max_length=255)
    stylist = models.ForeignKey('Employee', on_delete=models.PROTECT, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.PROTECT)
    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return f"{self.pk}-{self.details}"
