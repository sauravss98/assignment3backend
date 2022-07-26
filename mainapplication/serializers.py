from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserDetail
        fields=['id','userName','userEmail','userContactNumber','userAge','createdAt','updatedAt','password']
