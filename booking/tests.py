from django.test import TestCase
from booking.forms import BookingForm
from datetime import date

# Create your tests here.

class TestBookingForm(TestCase):

    def test_valid_form(self):
        form_data = {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'room_type': 'single',
            'check_in': date.today(),
            'check_out': date.today(),
            'special_requests': 'Quiet room please',
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        form_data = {
            'email': 'john@example.com',
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)
        self.assertIn('room_type', form.errors)
