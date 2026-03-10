from django.contrib import admin
from .models import Service, Appointment


# admin.site.register(Service)
# admin.site.register(Appointment)
#______________________________________________________________________
#
# Register the Service model in the admin panel
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    # Show these columns in the service list
    list_display = ('id', 'name', 'duration')

    # Allow searching services by name
    search_fields = ('name',)


# Register the Appointment model in the admin panel
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    # Columns shown in the appointment list
    list_display = (
        'id',
        'client',
        'employee',
        'service',
        'appointment_at',
        'status'
    )

    # Filters shown in the right sidebar
    list_filter = ('status', 'service')

    # Enable searching appointments by client or employee username
    search_fields = ('client__username', 'employee__username')
    