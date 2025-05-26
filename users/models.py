from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    # Removed gender from here, will be part of PatientProfile

    def __str__(self):
        return f"{self.username} ({self.role})"

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctorprofile')
    specialization = models.CharField(max_length=100)
    years_of_experience = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.user.username} ({self.specialization})"

class PatientProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('rather_not_specify', 'Rather Not Specify'),
    ]
    BLOOD_TYPE_CHOICES = [ # Example, you can expand this
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patientprofile')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='rather_not_specify')
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"Patient: {self.user.username}"
