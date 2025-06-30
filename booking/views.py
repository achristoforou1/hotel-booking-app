from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .forms import BookingForm
from .models import Booking

# Create your views here.

def home(request):
    """
    Renders the homepage.

    template: `home.html`
    """
    return render(request, 'home.html')

@login_required
def booking_view(request):
    """
    Renders the booking form and handles booking creation.

    model: `Booking`
    form: `BookingForm`

    context:
    - ``form``: Instance of BookingForm for user input

    template: `booking/booking_form.html`
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def my_bookings(request):
    """
    Displays all bookings made by the logged-in user.

    model: `Booking`

    context:
    - ``bookings``: List of Booking instances for the current user

    template: `booking/my_bookings.html`
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    """
    Allows the logged-in user to edit their booking.

    model: `Booking`
    form: `BookingForm`

    context:
    - ``form``: Pre-populated form with booking data

    template: `booking/edit_booking.html`
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/edit_booking.html', {'form': form})

@login_required
def delete_booking(request, booking_id):
    """
    Allows the logged-in user to delete one of their bookings.

    model: `Booking`

    context:
    - ``booking``: The Booking instance to confirm deletion

    template: `booking/delete_booking.html`
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')
    return render(request, 'booking/delete_booking.html', {'booking': booking})

def booking_success(request):
    """
    Displays a success message after a booking is submitted.

    template: `booking/booking_success.html`
    """
    return render(request, 'booking/booking_success.html')

