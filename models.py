
from django.db import models

# Tourist model
class Tourist(models.Model):
    name = models.CharField(max_length=100)
    tourist_id = models.CharField(max_length=50, unique=True)
   
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    emergency_contact_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


# Incident model
class Incident(models.Model):
    # Proper ForeignKey relationship with Tourist
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, related_name="incidents")

    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='incidents/', null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.tourist.name})"

class DangerZone(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField(help_text="Radius in meters")

    def __str__(self):
        return self.name

# api/models.py
class PanicAlert(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

