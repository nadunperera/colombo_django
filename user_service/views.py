#this is default django view import, which I do not need.
#from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from .models import User
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer