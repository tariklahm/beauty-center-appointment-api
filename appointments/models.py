from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

# services Model
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
# Appointment Model
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_appointments')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_appointments')
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    appointment_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['employee', 'appointment_at']

    def __str__(self):
        return f"{self.client} - {self.service} - {self.appointment_at}"