from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields= ['username', 'email', 'phone_number', 'address', 'pin_code', 'city', 'country', 'password']
        extra_kwargs={'password': {'write_only': True}}

    
    def create(self, validated_data):
        user=CustomUser.objects.create_user(**validated_data)
        return user 

    