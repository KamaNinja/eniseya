from django import forms

from .models import ServiceCategory, Employee


class FilterGalleryForm(forms.Form):
    service_category = forms.ModelMultipleChoiceField(
        queryset=ServiceCategory.objects.filter(gallery__is_active=True).distinct(),
        to_field_name='slug',
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'size': 10}),
        label='Категории услуг'
    )

    employee = forms.ModelMultipleChoiceField(
        queryset=Employee.active_objects.filter(gallery__is_active=True).distinct(),
        to_field_name='slug',
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'size': 10}),
        label='Мастера'
    )

    @staticmethod
    def filter_gallery(gallery, service_categories=None, employees=None):
        gallery = gallery.active_objects.all()
        if employees:
            gallery = gallery.filter(stylist__slug__in=employees)
        if service_categories:
            gallery = gallery.filter(service_category__slug__in=service_categories)
        return gallery
