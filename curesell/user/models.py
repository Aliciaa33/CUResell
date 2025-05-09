from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=30,default='')
    rate = models.FloatField(default=5.0)
    rate_number = models.FloatField(default=0)
