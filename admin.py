from django.contrib import admin
from .models import Tourist, Incident, DangerZone

# Tourist admin
@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tourist_id', 
                    'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_email')
    search_fields = ('name', 'tourist_id', 'emergency_contact_name',
                     'emergency_contact_phone', 'emergency_contact_email')

# Incident admin
@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'tourist', 'title', 'latitude', 'longitude', 'timestamp')
    search_fields = ('title', 'description', 'tourist__name', 'tourist__tourist_id')

# DangerZone admin
@admin.register(DangerZone)
class DangerZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude', 'radius')
    search_fields = ('name',)

from django.contrib.auth.models import User, Group

if User not in admin.site._registry:
    admin.site.register(User)

if Group not in admin.site._registry:
    admin.site.register(Group)
