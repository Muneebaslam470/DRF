from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer,PersonModelSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','PUT','PATCH'])
def singleobj(request,id):
    data = get_object_or_404(Person,id=id) 
    if request.method == "PUT":
        parsed_data = request.data
        serializer = PersonModelSerializer(data,data=parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"update":"success"})
      
    if request.method == "PATCH":
        parsed_data = request.data
        serializer = PersonModelSerializer(data,data=parsed_data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"update":"success"})

    if request.method == "GET": 
        serializer = PersonModelSerializer(data)
        return Response(serializer.data)


@api_view(['GET','POST'])
def multipleobj(request):
    if request.method == "POST":
        parse_data = request.data
        serializer = PersonModelSerializer(data=parse_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"created":"successfull"},status=status.HTTP_201_CREATED)
       
    if request.method == "GET": 
        print(request.accepted_renderer)    
        data = Person.objects.all()
        serializer = PersonModelSerializer(data,many=True)
        return Response(serializer.data)

