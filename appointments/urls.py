from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = router.urls