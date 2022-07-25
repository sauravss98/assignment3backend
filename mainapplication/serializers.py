from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','userName','userEmail','userContactNumber','userAge','createdAt','updatedAt')
        model=models.UserDetail