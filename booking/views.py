from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import BookingForm
from .models import Booking

# Create your views here.


@login_required
def booking_view(request):
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
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

def booking_success(request):
    return render(request, 'booking/booking_success.html')

