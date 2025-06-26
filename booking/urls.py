from django.urls import path, include
from . import views

urlpatterns = [
    path('book/', views.booking_view, name='booking_form'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('accounts/', include('allauth.urls')),

]
