from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import UserSerializer
# Create your views here.

class UserList(generics.ListAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer

