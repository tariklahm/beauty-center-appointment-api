# from rest_framework import viewsets
# from .models import Service, Appointment
# from .serializers import ServiceSerializer, AppointmentSerializer


# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer


# class AppointmentViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

from .models import Service, Appointment
from .serializers import ServiceSerializer, AppointmentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny, IsAdminUser

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Appointment.objects.all()

        return Appointment.objects.filter(client=user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    # CLIENT: view their appointments
    @action(detail=False, methods=['get'])
    def my(self, request):
        appointments = Appointment.objects.filter(client=request.user)
        serializer = self.get_serializer(appointments, many=True)
        return Response(serializer.data)

    # EMPLOYEE: view assigned appointments
    @action(detail=False, methods=['get'])
    def assigned(self, request):
        appointments = Appointment.objects.filter(employee=request.user)
        serializer = self.get_serializer(appointments, many=True)
        return Response(serializer.data)

    # CLIENT: cancel appointment (24h rule)
    @action(detail=True, methods=['patch'])
    def cancel(self, request, pk=None):
        appointment = self.get_object()

        if appointment.client != request.user:
            return Response({"error": "Not your appointment"}, status=403)

        if appointment.appointment_at - timezone.now() < timedelta(hours=24):
            return Response(
                {"error": "Appointments can only be cancelled 24h before"},
                status=400
            )

        appointment.status = "cancelled"
        appointment.save()

        return Response({"message": "Appointment cancelled"})