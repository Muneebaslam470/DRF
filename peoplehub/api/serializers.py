from rest_framework import serializers
from .models import Person

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','user','name','age','city']
        read_only_fields = ['user']

   

        

