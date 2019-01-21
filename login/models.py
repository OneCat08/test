from django.db import models

# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=64)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)