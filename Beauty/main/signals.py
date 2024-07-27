from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import ServiceCategory, Employee
from .utils import get_unique_slug


@receiver(pre_save, sender=ServiceCategory)
def create_slug(sender, instance, **kwargs):
    instance.slug = get_unique_slug(ServiceCategory, instance.title)


@receiver(pre_save, sender=Employee)
def create_slug(sender, instance, **kwargs):
    instance.slug = get_unique_slug(Employee, instance.name)
