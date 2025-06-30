from django.test import TestCase
from booking.forms import BookingForm
from booking.models import Booking
from django.urls import reverse
from datetime import date


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


# View testing
class TestBookingViews(TestCase):

    def test_booking_view_get(self):
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_form.html')

    def test_booking_view_post_success(self):
        form_data = {
            'full_name': 'Alice Smith',
            'email': 'alice@example.com',
            'room_type': 'double',
            'check_in': date.today(),
            'check_out': date.today(),
            'special_requests': 'Late check-in',
        }
        response = self.client.post(reverse('booking'), data=form_data)
        self.assertRedirects(response, reverse('booking_success'))

    def test_booking_success_view(self):
        response = self.client.get(reverse('booking_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_success.html')
