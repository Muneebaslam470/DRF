from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)
        
        if user is not None:
           token, created = Token.objects.get_or_create(user=user)
           return Response({'token':token.key})
        return Response({'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)    
    