from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.

    Displays the following fields in the admin list view:
    - full_name
    - email
    - room_type
    - check_in
    - check_out

    Enables admin search functionality by:
    - full_name
    - email
    """
    list_display = ('full_name', 'email', 'room_type', 'check_in', 'check_out')
    search_fields = ('full_name', 'email')
