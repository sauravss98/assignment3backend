from django.db import models

# Create your models here.

class UserDetail(models.Model):
    userName=models.CharField(max_length=200)
    userEmail=models.EmailField()
    userContactNumber=models.IntegerField()
    userAge=models.IntegerField()
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userName