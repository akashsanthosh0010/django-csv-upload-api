from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'age']


    def validate_age(self, age):
        if not(0 <= age <= 120):
            raise serializers.ValidationError("Age must be above 0 and below 120 ")
        return age

