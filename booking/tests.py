from django.test import TestCase
from booking.forms import BookingForm
from booking.models import Booking
from datetime import date

# Create your tests here.

# Form Tests
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

# Model Tests
class BookingModelTest(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(
            full_name="John Doe",
            email="john@example.com",
            room_type="double",
            check_in=date(2025, 7, 1),
            check_out=date(2025, 7, 5),
            special_requests="High floor"
        )

    def test_booking_str_method(self):
        self.assertEqual(str(self.booking), "John Doe (double)")

    def test_booking_fields(self):
        self.assertEqual(self.booking.room_type, "double")
        self.assertEqual(self.booking.check_in, date(2025, 7, 1))
