from django.db import models

# Room type options
ROOM_CHOICES = [
    ('single', 'Single Room'),
    ('double', 'Double Room'),
    ('suite', 'Suite'),
]

# Create your models here.

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    check_in = models.DateField()
    check_out = models.DateField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.room_type})"