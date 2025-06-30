from django.db import models
from django.contrib.auth.models import User


# Room type options
ROOM_CHOICES = [
    ('single', 'Single Room'),
    ('double', 'Double Room'),
    ('suite', 'Suite'),
]


class Booking(models.Model):
    """
    model: Booking

    Represents a room booking made by a user.

    Related model:
    - `User`: Linked via ForeignKey to identify which user made the booking.

    Fields:
    - full_name: Full name of the guest
    - email: Contact email of the guest
    - room_type: Type of room selected (choices defined in ROOM_CHOICES)
    - check_in: Date of check-in
    - check_out: Date of check-out
    - special_requests: Any optional notes or requests for the booking
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    check_in = models.DateField()
    check_out = models.DateField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.room_type})"
