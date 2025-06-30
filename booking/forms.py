from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    form: BookingForm

    Handles user input for creating and editing room bookings.

    Fields:
    - room_type: Dropdown for selecting room type
    - check_in: Date field for the check-in date
    - check_out: Date field for the check-out date
    - special_requests: Optional text input for any special needs

    Validation:
    - Ensures check-out date is after check-in date
    """

    class Meta:
        model = Booking
        fields = ['room_type', 'check_in', 'check_out', 'special_requests']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out and check_out <= check_in:
            self.add_error(
                None,
                "WARNING: Check-out date MUST be after check-in date."
            )
