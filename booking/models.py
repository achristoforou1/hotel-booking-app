from django.db import models
from django.contrib.auth.models import User


# Room type options
ROOM_CHOICES = [
    ('single', 'Single Room'),
    ('double', 'Double Room'),
    ('suite', 'Suite'),
]

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    check_in = models.DateField()
    check_out = models.DateField()
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.room_type})"