from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Incident
        fields= ['incident_id', 'entity', 'details', 'reported_date', 'priority', 'status', 'reporter']
        read_only_fields=['incident_id', 'reported_date', 'reporter']
        