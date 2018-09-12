#this is default django view import, which I do not need.
#from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from . import models
from . import serializers

class UserListCreate(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
