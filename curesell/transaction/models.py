from django.db import models
from user.models import UserInfo
from product.models import ProductInfo

# Create your models here.
class Transaction(models.Model):
    buyer = models.ForeignKey(UserInfo, on_delete=models.CASCADE, default='')
    product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, default='')
    date = models.DateTimeField((u"Conversation Time"),  auto_now_add=True)
    price = models.FloatField(default=0.0)
    rate = models.IntegerField(default=5)
