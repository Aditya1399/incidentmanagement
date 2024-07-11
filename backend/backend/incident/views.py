from rest_framework import generics
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class IncidentCreateView(generics.CreateAPIView):
    serializer_class=IncidentSerializer
    permission_class=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)



class IncidentListView(generics.ListAPIView):
    serializer_class=IncidentSerializer
    permission_class=[IsAuthenticated]


    def get_queryset(self):
        return Incident.objects.filter(reporter=self.request.user)


class IncidentDetailView(generics.RetrieveUpdateAPIView):
    serializer_class=IncidentSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(reporter=self.request.user)
        