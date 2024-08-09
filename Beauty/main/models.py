from django.core.validators import MinValueValidator
from django.db import models

from .utils import UniqueNameImageModelMixin


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ServiceCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                blank=True,
                                null=True,
                                validators=[MinValueValidator(0.1)],
                                verbose_name='Цена')
    duration = models.PositiveSmallIntegerField(blank=True,
                                                null=True,
                                                verbose_name='Длительность')
    is_active = models.BooleanField(default=True, verbose_name='Статус')
    service_category = models.ForeignKey('ServiceCategory',
                                         on_delete=models.PROTECT,
                                         verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['service_category', 'title']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Employee(UniqueNameImageModelMixin, models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    details = models.CharField(max_length=255, verbose_name='Описание')
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    is_active = models.BooleanField(default=True, verbose_name='Статус')
    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Gallery(UniqueNameImageModelMixin, models.Model):
    details = models.CharField(max_length=255, verbose_name='Описание')
    stylist = models.ForeignKey('Employee',
                                on_delete=models.PROTECT,
                                blank=True,
                                null=True,
                                verbose_name='Мастер')
    is_active = models.BooleanField(default=True, verbose_name='Статус')
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.PROTECT, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self):
        return f"{self.pk}-{self.details}"

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
