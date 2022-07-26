from django.db import models

# Create your models here.

class UserDetail(models.Model):
    userName=models.CharField(max_length=200)
    userEmail=models.EmailField()
    userContactNumber=models.IntegerField()
    userAge=models.IntegerField()
    password=models.CharField(max_length=20)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName


# class ProductDetails(models.Model):
#     Item=models.CharField(max_length=250)
#     BrandName=models.CharField(max_length=250)
#     QuantityLeft=models.IntegerField()
#     Offer=models.DecimalField()
#     ProductPrice=models.DecimalField()
#
#     def __str__(self):
#         return self.Item
