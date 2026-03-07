from django.contrib import admin
from .models import User


# Register the custom User model in Django Admin
# This allows us to manage users from the admin dashboard
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    # Columns displayed in the admin users list
    list_display = ('id', 'username', 'email', 'role', 'is_staff')

    # Filter options shown on the right side of the admin page
    list_filter = ('role', 'is_staff')

    # Enables search by username or email
    search_fields = ('username', 'email')