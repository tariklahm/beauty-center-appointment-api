# Beauty Center Appointment Management API
Project Overview

The Beauty Center Appointment Management API is a backend system designed to help beauty salons manage their services, employees, and client appointments.

The system allows clients to book appointments, employees to manage their schedules, and administrators to control services and users through a centralized API.

This project was developed as part of the ALX Backend Development Program using Django and Django REST Framework.

# Features

The API provides the following features:
User authentication
Service management
Appointment booking
Employee assignment
Appointment status tracking
Role-based user system (Client, Employee, Admin)

# Technologies Used

Python
Django
Django REST Framework
SQLite
Simple JWT

# API Endpoints
- Authentication
/api/auth/login/    
or 
/api-auth/login/
/api/auth/token/refresh/
Services
GET     /api/services/
POST    /api/services/
GET     /api/services/{id}/
- Appointments
GET     /api/appointments/
POST    /api/appointments/
GET     /api/appointments/my/
GET     /api/appointments/assigned/
PATCH   /api/appointments/{id}/cancel/
- User Roles
The system defines three user roles:
Role	  Description
Client	  Can book appointments
Employee  Handles assigned appointments
Admin	  Manages users, services, and appointments
- Admin Panel

The system includes the Django admin panel for managing data.
Access it here:
http://127.0.0.1:8000/admin/

# Future Improvements

Possible improvements include:
Email notifications for appointments
Payment integration
Calendar scheduling
Frontend interface

Author
Tarik LAHMAM
ALX Backend Web Development Student