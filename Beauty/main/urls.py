from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.get_services, name='services'),
    path('employees/', views.get_employees, name='employees'),
    path('gallery/', views.get_gallery, name='gallery'),
]
