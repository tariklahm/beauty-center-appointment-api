from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Service, Appointment

User = get_user_model()


# Serializer for Service model
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


# Serializer for Appointment model
class AppointmentSerializer(serializers.ModelSerializer):

    # Show client's username instead of ID
    client = serializers.ReadOnlyField(source='client.username')

    # Only show users with role "employee"
    employee = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role="employee")
    )

    class Meta:
        model = Appointment
        fields = [
            'id',
            'client',
            'employee',
            'service',
            'appointment_at',
            'status',
            'created_at'
        ]

        read_only_fields = ['status', 'created_at']

    # Validate that the appointment date is in the future
    def validate_appointment_at(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "Appointment must be scheduled in the future."
            )
        return value

    # Prevent double booking
    def validate(self, data):
        employee = data['employee']
        appointment_at = data['appointment_at']

        if Appointment.objects.filter(
            employee=employee,
            appointment_at=appointment_at
        ).exists():
            raise serializers.ValidationError(
                "This employee already has an appointment at this time."
            )

        return data