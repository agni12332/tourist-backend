from rest_framework import routers
from django.urls import path, include
from .views import (
    TouristViewSet,
    IncidentViewSet,
    DangerZoneViewSet,
    PanicAlertViewSet,
    report_incident
)

# DRF router for ViewSets
router = routers.DefaultRouter()
router.register(r'tourists', TouristViewSet)
router.register(r'incidents', IncidentViewSet)
router.register(r'dangerzones', DangerZoneViewSet)
router.register(r'panicalerts', PanicAlertViewSet)



urlpatterns = [
    # Include DRF router URLs
    path('', include(router.urls)),
    
    # Function-based DRF view
    path('report-incident/', report_incident, name='report-incident'),
]

