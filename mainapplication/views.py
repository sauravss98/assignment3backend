from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.parsers import FormParser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.

class UserList(ListAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        # userName = request.data['userName']
        # userEmail = request.data['userEmail']
        # userContactNumber = request.data['userContactNumber']
        # userAge = request.data['userAge']
        # createdAt = request.data['createdAt']
        # updatedAt = request.data['updatedAt']
        # user = UserDetail.objects.get(userName=userName, userEmail=userEmail, userContactNumber=userContactNumber,
        #                                   userAge=userAge, createdAt=createdAt, updatedAt=updatedAt)
        # user.save()
        # return HttpResponse({'message': "Uploaded"}, status=200)


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer
