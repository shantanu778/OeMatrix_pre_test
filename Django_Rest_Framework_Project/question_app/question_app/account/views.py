from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .serializer import UserCreateSerializer, UserGetSerializer


@api_view(['POST',])
def signup(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save() 
            data['email'] = user.email
            data['username'] =user.username
            data['token'] = Token.objects.get(user= user).key
            data['message'] = "User Registration Successfully"
        else:
            data = serializer.errors
    
        return Response(data)        
    

@api_view(['GET',])
def users(request):
    if request.method == 'GET':
        users = User.objects.all().order_by("id")
        serializer = UserGetSerializer(users, many=True)
        return Response(serializer.data)