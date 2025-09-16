# api/serializers.py
from rest_framework import serializers
from .models import Tourist, Incident, DangerZone
from .models import PanicAlert

class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class DangerZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DangerZone
        fields = '__all__'


class PanicAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanicAlert
        fields = '__all__'
