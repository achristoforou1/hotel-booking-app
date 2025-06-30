from django.apps import AppConfig


class BookingConfig(AppConfig):
    """
    App configuration for the booking application.
    Sets the default name for the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
