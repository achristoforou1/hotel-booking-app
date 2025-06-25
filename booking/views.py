from django.shortcuts import render, redirect
from .forms import BookingForm

# Create your views here.

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'booking/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'booking/booking_success.html')

