from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserDetail
        fields=['id','userName','userEmail','userContactNumber','userAge','password']


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model=ProductDetails
        fields=['id','itemName','brandName','offer','quantityLeft','price','imageURL']