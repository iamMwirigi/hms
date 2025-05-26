from django.db import models
from users.models import User # Or PatientProfile, DoctorProfile for more specific links

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

  
    patient = models.ForeignKey(User, related_name='patient_appointments', on_delete=models.CASCADE, limit_choices_to={'role': 'patient'})
    doctor = models.ForeignKey(User, related_name='doctor_appointments', on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'})
    appointment_time = models.DateTimeField()
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.patient.username} with {self.doctor.username} at {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(User, related_name='medical_records', on_delete=models.CASCADE, limit_choices_to={'role': 'patient'})
    doctor = models.ForeignKey(User, related_name='authored_medical_records', on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'})
    appointment = models.ForeignKey(Appointment, related_name='medical_records', on_delete=models.CASCADE)
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.patient.username} from appointment {self.appointment.id}"

class Bill(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='bill')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')
    issued_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Bill for Appointment {self.appointment.id} - Amount: {self.total_amount}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False) # Added for tracking

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.sent_at.strftime('%Y-%m-%d %H:%M')}"

