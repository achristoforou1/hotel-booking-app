from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.booking_view, name='booking_form'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path("accounts/password/reset/", auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html"
    ), name="account_reset_password"),

    
]
