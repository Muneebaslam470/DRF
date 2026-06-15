from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)
        model = User
        fields = ['username','password','email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
