from django.urls import path 
from .views import IncidentCreateView, IncidentListView, IncidentDetailView

urlpatterns=[
    path('', IncidentListView.as_view(), name='incident-list'),
    path('create/', IncidentCreateView.as_view(), name='incident-create'),
    path('<int:pk/', IncidentDetailView.as_view(), name='incident-detail'),

]