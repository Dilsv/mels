# services/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/edit/<int:booking_id>/', views.booking_edit, name='booking_edit'),
    path('bookings/delete/<int:booking_id>/', views.booking_delete, name='booking_delete'),
]
