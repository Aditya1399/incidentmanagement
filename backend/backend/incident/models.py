from django.db import models
from user.models import CustomUser
import random 
import datetime
from backend import settings
# Create your models here.
class Incident(models.Model):
    ENTERPRISE='enterprise'
    GOVERNMENT='Government'
    ENTITY_CHOICES=[
        (ENTERPRISE, 'Enterprise'),
        (GOVERNMENT, 'Government'),
    ]
    PRIORITY_HIGH='High'
    PRIORITY_MEDIUM= 'Medium'
    PRIORITY_LOW= 'Low'

    PRIORITY_CHOICES= [
        (PRIORITY_HIGH, 'High'),
        (PRIORITY_MEDIUM, 'Medium'),
        (PRIORITY_LOW, 'Low'),
    ]
    STATUS_OPEN='Open'
    STATUS_IN_PROGRESS= 'In Progress'
    STATUS_CLOSED= 'Closed'
    STATUS_CHOICES = [
        (STATUS_OPEN, 'Open'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_CLOSED, 'Closed'),
    ]

    reporter=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    incident_id= models.CharField(max_length=15, unique=True, default=True)
    entity= models.CharField(max_length=50, choices= ENTITY_CHOICES)
    details=models.TextField()
    reported_data= models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status= models.CharField(max_length=15, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if not self.incident_id:
            self.incident_id= f'RMG{random.randint(10000, 99999)}{datetime.datetime.now().year}'
        super().save(*args, **kwargs)


