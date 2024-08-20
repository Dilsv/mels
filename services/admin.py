from django.contrib import admin

# Register your models here.

from .models import Booking

class BookingAdmin (admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
    )


admin.site.register (
    Booking, BookingAdmin
)