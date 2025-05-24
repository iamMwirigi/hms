from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('rather_not_specify', 'Rather Not Specify'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='rather_not_specify')
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
