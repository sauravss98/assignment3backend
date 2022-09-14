from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from rest_framework import generics, status
from rest_framework.parsers import FormParser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



class UserList(generics.ListAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer

class CreateUser(generics.CreateAPIView):
    serializer_class=UserSerializer

class UpdateUser(generics.UpdateAPIView):
    serializer_class=UserSerializer
    queryset=UserDetail.objects.all()

class DeleteUser(generics.DestroyAPIView):
    model=UserDetail
    queryset=UserDetail.objects.all()

# class UserDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserDetail.objects.all()
#     serializer_class = UserSerializer

class ProductList(ListAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductSerializer

    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductSerializer