from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=30,default='')
    contact_link = models.CharField(max_length=40,default='')
    rate = models.FloatField(default=5.0)
