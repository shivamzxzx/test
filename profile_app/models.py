from django.db import models

# Create your models here.
from rest_framework.authtoken.admin import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    pincode = models.IntegerField()
    profile_pic = models.TextField()