# services/models.py

from django.db import models
from django.contrib.auth.models import User  # Import User model

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('natural', 'Natural Makeup'),
        ('glam', 'Glam Makeup'),
        ('bridal', 'Bridal Makeup'),
        ('hd', 'HD Makeup'),
    ]
    
    # Associate booking with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add ForeignKey to User

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service} on {self.date} at {self.time}"
