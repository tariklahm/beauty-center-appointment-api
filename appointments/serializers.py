from rest_framework import serializers
from django.utils import timezone
from .models import Service, Appointment


# Serializer for Service model
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # Return all fields of the Service model
        fields = '__all__'


# Serializer for Appointment model
class AppointmentSerializer(serializers.ModelSerializer):

    # Show the client's username instead of the client ID
    # The client field will be filled automatically from request.user
    client = serializers.ReadOnlyField(source='client.username')

    class Meta:
        model = Appointment

        # Fields that will appear in API responses
        fields = [
            'id',               # Appointment ID
            'client',           # Username of the client who booked
            'employee',         # Employee assigned to the appointment
            'service',          # Service requested
            'appointment_at',   # Date and time of the appointment
            'status',           # Appointment status (scheduled, completed, cancelled)
            'created_at'        # When the appointment was created
        ]

        # Fields that cannot be modified by the user
        read_only_fields = ['status', 'created_at']

    # Validate that the appointment date is in the future
    def validate_appointment_at(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "Appointment must be scheduled in the future."
            )
        return value

    # General validation for the appointment
    def validate(self, data):
        employee = data['employee']
        appointment_at = data['appointment_at']

        # Prevent double booking for the same employee at the same time
        if Appointment.objects.filter(
            employee=employee,
            appointment_at=appointment_at
        ).exists():
            raise serializers.ValidationError(
                "This employee already has an appointment at this time."
            )

        return data