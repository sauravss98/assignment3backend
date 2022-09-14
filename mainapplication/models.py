from django.db import models

# Create your models here.

class UserDetail(models.Model):
    userName=models.CharField(max_length=200)
    userEmail=models.EmailField()
    userContactNumber=models.IntegerField()
    userAge=models.IntegerField()
    password=models.CharField(max_length=20)
    # createdAt=models.DateTimeField(auto_now_add=True)
    # updatedAt=models.DateTimeField(auto_now_add=True)

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


class ProductDetails(models.Model):
    itemName=models.CharField(max_length=255)
    brandName=models.CharField(max_length=255)
    offer=models.IntegerField()
    quantityLeft=models.IntegerField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    imageURL=models.CharField(max_length=100000)

    def __str__(self):
        return self.itemName