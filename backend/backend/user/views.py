from rest_framework import generics, views 
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
import requests 



class UserCreateView(generics.CreateAPIView):
    queryset= CustomUser.objects.all()
    serializer_class= UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset= CustomUser.objects.all()
    serializer_class= UserSerializer

